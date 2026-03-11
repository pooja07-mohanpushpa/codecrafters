from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import CodingProblem, TestCase, UserSubmission
from users.models import UserProfile
import json
import traceback
import sys
from io import StringIO

@login_required
def arena_home(request):
    first_problem = CodingProblem.objects.order_by('order', 'created_at').first()
    if first_problem:
        from django.shortcuts import redirect
        return redirect('arena_problem', slug=first_problem.slug)
    problems = CodingProblem.objects.all()
    context = {
        'problems': problems,
    }
    return render(request, 'arena/arena.html', context)

@login_required
def problem_detail(request, slug):
    problem = get_object_or_404(CodingProblem, slug=slug)
    problems = CodingProblem.objects.all()
    
    test_cases_list = list(problem.test_cases.values('input_data', 'expected_output'))
    
    context = {
        'problem': problem,
        'problems': problems,
        'test_cases_json': json.dumps(test_cases_list)
    }
    return render(request, 'arena/arena.html', context)


@login_required
def submit_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code')
        lang = data.get('language')
        problem_id = data.get('problem_id')
        
        # New frontend-driven fields
        passed = data.get('passed', 0)
        total = data.get('total', 0)
        status = data.get('status', 'Failed')
        results = data.get('results', [])
        
        problem = get_object_or_404(CodingProblem, id=problem_id)

        # Save submission
        submission = UserSubmission.objects.create(
            user=request.user,
            problem=problem,
            code=code,
            language=lang,
            status=status,
            passed_test_cases=passed,
            total_test_cases=total,
            result_details=json.dumps(results)
        )

        # Award points if passed all — but only on FIRST success
        already_passed = UserSubmission.objects.filter(
            user=request.user, problem=problem, status="Passed"
        ).exclude(id=submission.id).exists()

        if status == "Passed" and not already_passed:
            profile = request.user.profile
            # Arena points disabled per user request — Points now come only from Quizzes
            # profile.code_points += problem.points_reward
            profile.challenges_solved += 1
            profile.save()
            return JsonResponse({
                'status': 'Passed',
                'message': 'Congratulations! You passed all test cases. (Points are now earned from Quizzes only)',
                'results': results
            })
        elif status == "Passed" and already_passed:
            return JsonResponse({
                'status': 'Passed',
                'message': f'All test cases passed! (Points already earned for this problem.)',
                'results': results
            })
        else:
            return JsonResponse({
                'status': 'Failed',
                'message': f'Only {passed}/{total} test cases passed. Try again!',
                'results': results
            })

