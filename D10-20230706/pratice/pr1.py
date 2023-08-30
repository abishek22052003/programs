# marks=[96,33,66,44,66]
# #enum_marks=enumerate(marks)
# total_marks=0
# for i,mark in enumerate(marks):
#     print("entering iteration process in mark "+str(mark))
#     print("before sum",total_marks)
#     total_marks=total_marks+mark
#     print("after sum ",total_marks)
#     print("\n")

marks=[96,33,66,44,66]
# #enum_marks=enumerate(marks)
total_marks=0
# for i,mark in enumerate(marks):
#     print(f"entering iteration process in mark {str(mark)}")
#     print("brfore_sum",total_marks)
#     total_marks=total_marks+mark
#     print("after sum",total_marks)
for mark in marks:
    print("before add",total_marks)
    total_marks=total_marks+mark
    print("after add",total_marks)
print("total mark is",total_marks)
    