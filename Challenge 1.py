# These are the number of [As, Bs, Cs, Ds, Es, Fs]
marks_class_A = [6, 5, 7, 4, 3, 0]
marks_class_B = [9, 8, 3, 1, 2, 3]

import matplotlib.pyplot as plt
plt.figure(figsize=(3,3))
plt.bar(["A","B","C", "D", "E", "F"], marks_class_A, color='green')
plt.grid(color="grey", linestyle='--', linewidth=2, axis='y', alpha=0.1)
plt.savefig("Plot1.png")
plt.show()

# plt.bar(["A","B","C", "D", "E", "F"], marks_class_B, color='Blue')
# plt.grid(color="grey", linestyle='--', linewidth=2, axis='y', alpha=0.1)
# plt.savefig("Plot2.png")
# plt.show()

# plt.bar(["A","B","C", "D", "E", "F"], marks_class_A, color='red', bottom=marks_class_B)
# plt.bar(["A","B","C", "D", "E", "F"], marks_class_B, color='orange')
# plt.grid(color='blue', linestyle='--', linewidth=2, axis='y', alpha=0.7)
# plt.xlabel('Class')
# plt.ylabel('Amounts')
# plt.title("Title")
# plt.savefig("Plot3.png")
# plt.show()

# Labels=["A","B","C", "D", "E", "F"]
# plt.bar([1,2,3,4,5,6], marks_class_A, color='red', width=.2)

# plt.bar([1.2,2.2,3.2,4.2,5.2,6.2], marks_class_B, color='orange', width=-.2)
# plt.grid(color='blue', linestyle='--', linewidth=2, axis='y', alpha=0.7)
# plt.xticks([1,2,3,4,5,6], ["A","B","C", "D", "E", "F"])
# plt.xlabel('Class')
# plt.ylabel('Amounts')
# plt.title("Title")
# plt.savefig("Plot4.png")
# plt.show()
