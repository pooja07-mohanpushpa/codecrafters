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
    context = {
        'problem': problem,
        'problems': problems,
    }
    return render(request, 'arena/arena.html', context)

@login_required
def run_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code')
        lang = data.get('language')
        input_data = data.get('input', '')

        # Mock execution logic
        # In a real app, this would use a sandbox API (Piston, Judge0, etc.)
        if lang == 'python':
            output, error = execute_python(code, input_data)
            return JsonResponse({'output': output, 'error': error})
        else:
            return JsonResponse({'output': f"Execution for {lang} is mocked in this demo environment.\nOutput: Success!", 'error': ''})

@login_required
def submit_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code')
        lang = data.get('language')
        problem_id = data.get('problem_id')
        
        problem = get_object_or_404(CodingProblem, id=problem_id)
        test_cases = problem.test_cases.all()
        
        passed = 0
        total = test_cases.count()
        results = []

        # Simplified judging for demo
        for tc in test_cases:
            if lang == 'python':
                output, error = execute_python(code, tc.input_data)
                # Clean up output for comparison
                cleaned_output = output.strip().replace("'", '"')
                expected = tc.expected_output.strip().replace("'", '"')
                
                status = "Passed" if cleaned_output == expected else "Failed"
                if status == "Passed":
                    passed += 1
                results.append({
                    'input': tc.input_data,
                    'expected': tc.expected_output,
                    'actual': output,
                    'status': status
                })
            else:
                # Mock pass for other languages if code is present
                passed += 1
                results.append({
                    'input': tc.input_data,
                    'expected': tc.expected_output,
                    'actual': tc.expected_output,
                    'status': "Passed"
                })

        # Save submission
        status = "Passed" if passed == total else "Failed"
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
            profile.code_points += problem.points_reward
            profile.challenges_solved += 1
            profile.save()
            return JsonResponse({
                'status': 'Passed',
                'message': f'Congratulations! You passed all test cases and earned {problem.points_reward} CodePoints.',
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


def execute_python(code, input_data):
    """
    EXTREMELY INSECURE - USE ONLY FOR LOCAL DEMO.
    Runs python code using exec() and captures output.
    """
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    
    # Mock input() for simple scripts
    # This is a crude way to handle inputs in exec()
    mock_vars = {'input_data': input_data}
    
    try:
        # We try to inject a simple input override for specific problems
        # Or just append the input data to a variable the user might use
        # For 'Two Sum', user might expect nums and target as variables
        # Since we can't easily parse arbitrary test case formats into variables,
        # we'll assume the problem descriptions define how to read input.
        
        exec(code, {}, mock_vars)
        output = redirected_output.getvalue()
    except Exception:
        output = traceback.format_exc()
        return "", output
    finally:
        sys.stdout = old_stdout
        
    return output, ""
