# Assignment-3: Build Your Own Quiz Game (MCQ Version)

def quiz_game():
    print("🎯 Welcome to Python Interview Prep Quiz 🎯")
    print("You will be asked 20 questions. Each has 4 options.\n")

    # 20 MCQ Questions with options
    questions = [
        {
            "q": "What is the keyword to define a function in Python?",
            "options": ["func", "def", "function", "define"],
            "a": "def"
        },
        {
            "q": "What is the output of 2 ** 3 in Python?",
            "options": ["6", "9", "8", "5"],
            "a": "8"
        },
        {
            "q": "Which keyword is used for loops in Python?",
            "options": ["for", "loop", "iterate", "while"],
            "a": "for"
        },
        {
            "q": "What is the data type of [1,2,3] ?",
            "options": ["tuple", "list", "set", "dict"],
            "a": "list"
        },
        {
            "q": "Which symbol is used for comments in Python?",
            "options": ["//", "#", "/*", "--"],
            "a": "#"
        },
        {
            "q": "What is the keyword to create a class in Python?",
            "options": ["object", "define", "class", "structure"],
            "a": "class"
        },
        {
            "q": "What function is used to get input from the user?",
            "options": ["scan()", "cin", "input()", "read()"],
            "a": "input()"
        },
        {
            "q": "Which operator is used for floor division?",
            "options": ["/", "//", "%", ""],
            "a": "//"
        },
        {
            "q": "What is the output of len('Python')?",
            "options": ["5", "7", "6", "8"],
            "a": "6"
        },
        {
            "q": "Which built-in function returns the data type of a variable?",
            "options": ["data()", "type()", "dtype()", "typeof()"],
            "a": "type()"
        },
        {
            "q": "What is the correct file extension for Python files?",
            "options": [".py", ".python", ".pyt", ".txt"],
            "a": ".py"
        },
        {
            "q": "Which function converts a string into an integer?",
            "options": ["str()", "int()", "float()", "eval()"],
            "a": "int()"
        },
        {
            "q": "What is the keyword to handle exceptions in Python?",
            "options": ["catch", "try", "except", "throw"],
            "a": "try"
        },
        {
            "q": "Which module is used for random number generation?",
            "options": ["math", "random", "numbers", "os"],
            "a": "random"
        },
        {
            "q": "What is the output of bool(0)?",
            "options": ["True", "False", "0", "None"],
            "a": "False"
        },
        {
            "q": "Which keyword is used to exit a loop prematurely?",
            "options": ["stop", "exit", "break", "end"],
            "a": "break"
        },
        {
            "q": "What is the method to add an element to a list?",
            "options": ["insert()", "append()", "add()", "push()"],
            "a": "append()"
        },
        {
            "q": "Which operator is used for exponentiation?",
            "options": ["^", "", "pow", "%"],
            "a": ""
        },
        {
            "q": "What is the default return value of a function that has no return statement?",
            "options": ["0", "null", "None", "undefined"],
            "a": "None"
        },
        {
            "q": "Which keyword is used to import modules in Python?",
            "options": ["package", "import", "include", "using"],
            "a": "import"
        }
    ]

    score = 0

    # Loop through questions
    for i, item in enumerate(questions, start=1):
        print(f"Q{i}: {item['q']}")
        for idx, opt in enumerate(item["options"], start=1):
            print(f"   {idx}. {opt}")
        ans = input("Enter option number (1-4): ").strip()

        # Validate answer
        if ans.isdigit() and 1 <= int(ans) <= 4:
            chosen = item["options"][int(ans)-1]
            if chosen.lower() == item["a"].lower():
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer is: {item['a']}\n")
        else:
            print("⚠ Invalid choice! Skipped.\n")

    # Final result
    print("🎉 Quiz Completed! 🎉")
    print(f"Your Score: {score} / {len(questions)}")
    if score >= 15:
        print("Excellent! You're well prepared for Python interviews.")
    elif score >= 10:
        print(" Good job! Keep practicing.")
    else:
        print("Needs improvement. Review Python basics again.")

# ✅ Call function
quiz_game()