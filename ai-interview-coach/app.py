A beginner Python project that evaluates interview answers using scoring rules, keyword detection, and structured feedback. 


def score_answer(answer):
 if len(answer) < 50:
  return 40, "Your answer is too short. Add more details and examples."
 elif len(answer) < 150:
  return 70, "Good start, but add specific results or achievements."
 else:
  return 90, "Good length. Now improve clarity and confidence."




def check_keywords(answer):
    answer_lower = answer.lower()


    strong_keywords = [
        "root cause",
        "corrective action",
        "countermeasure",
        "process improvement",
        "prevent recurrence",
        "downtime",
        "defects",
        "pfmea",
        "control plan",
        "sop",
        "5m analysis"
    ]


    count = 0


    for keyword in strong_keywords:
        if keyword in answer_lower:
            count += 1


    if count >= 4:
        return "Good: Strong engineering keywords and process improvement details detected."
    elif count >= 2:
        return "Good start: Add more measurable results such as downtime reduction, defect reduction, or yield improvement."
    else:
        return "Warning: Add stronger engineering reasoning, root cause analysis, and measurable results."




role = input("Enter target role: ")
answer = input("Paste your interview answer: ")
overall_score = 90




score, feedback = score_answer(answer)
keyword_feedback = check_keywords(answer)


print("\n--- Interview Feedback ---")
print(f"Target Role: {role}")
print(f"Your Answer: {answer}")
print(f"Confidence Score: {score}")
print(f"Feedback: {feedback}")
print(keyword_feedback)
print(f"Overall Score: {overall_score}")