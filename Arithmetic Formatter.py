def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        return 'Error: Too many problems.'
        
    for problem in problems:
        parts=problem.split()
        if not evaluate_expression(parts):
            return "Error: Operator must be '+' or '-'."
        if not check_digit(parts):
            return "Error: Numbers must only contain digits."
        if not check_length(parts):
            return 'Error: Numbers cannot be more than four digits.'
    arranged_problems = arrange_problems(problems, show_answers)
    
    return arranged_problems
    
def evaluate_expression(parts):
    op=parts[1]
    return op in ["+","-"]


def check_digit(parts):
    num1, num2 = parts[0], parts[2]
    return num1.isdigit() and num2.isdigit()

def check_length(parts):
    num1, num2 = parts[0], parts[2]
    return len(num1) <= 4 and len(num2) <= 4

def arrange_problems(problems, show_answers):
    first_row = ""
    second_row = ""
    dashes_row = ""
    results_row = ""
    results_row = ""
    for problem in problems:
        parts=problem.split()
        num1=parts[0]
        op=parts[1]
        num2=parts[2]
        width = max(len(num1), len(num2)) + 2
        if show_answers:
            if op=="+":
                result=int(num1)+int(num2)
            elif op=="-":
                result=int(num1)-int(num2)
            results_row += str(result).rjust(width) + "    "
        first_row += num1.rjust(width) + "    "
        second_row += op + num2.rjust(width - 1) + "    "
        dashes_row += "-" * width + "    "

    if show_answers:
        return f"{first_row.rstrip()}\n{second_row.rstrip()}\n{dashes_row.rstrip()}\n{results_row.rstrip()}"
    else:
        return f"{first_row.rstrip()}\n{second_row.rstrip()}\n{dashes_row.rstrip()}"
            




print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')