# ============================================================
#  Live Class 05  |  Example 01
#  One if - a warm-up from the last class
# ============================================================
#  Story:
#  If it is raining you take an umbrella. If it is not, you don't.
#  An if statement is how we tell the computer exactly that.
#
#  Things to remember:
#  - Lines that sit INSIDE the if (pushed in with spaces) run
#    only when the condition is true
#  - Lines inside else run when the condition is false
#  - Lines outside the if always run
# ============================================================

rain = "yes"                    # we write the value ourselves

if rain == "yes":               # the question Python asks
    print("Take an umbrella.")  # runs when the answer is yes
else:
    print("No umbrella today.")

print("Now go outside.")        # outside the if, so it always runs

# ============================================================
#  Expected Output:
#
#  Take an umbrella.
#  Now go outside.
# ============================================================
#  Try it yourself:
#  1) Change the first line to rain = "no" and run it again.
#     Which line changed? Which line stayed the same?
#  2) Put 4 spaces in front of the last print line.
#     Now run it with rain = "no". Does that line still appear?
# ============================================================
