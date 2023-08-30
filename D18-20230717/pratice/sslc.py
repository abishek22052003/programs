sslcs=[{"name":"ram","place":"kottar","sslc":{"tamil":100,"english":100,"maths":100,"science":96,"social":90}},
      {"name":"suresh","place":"vadasery","sslc":{"tamil":80,"english":62,"maths":100,"science":66,"social":70}},
      {"name":"ravi","place":"kanniyakumari","sslc":{"tamil":80,"english":82,"maths":78,"science":86,"social":90}},
      {"name":"abi","place":"kottar","sslc":{"tamil":70,"english":72,"maths":100,"science":56,"social":60}} ]
for sslc in sslcs:
    sl=sslc["sslc"]
    average=sl["tamil"]+sl["english"]+sl["maths"]+sl["science"]+sl["social"]
    percentage=(average/500)*100
    print(percentage)
    if percentage>90 or (percentage>75 and sl["maths"]>=98):
        print("You are eligible for maths biology")
    elif percentage>80 or (percentage>70 and sl["maths"]>=98):
        print("You are eligible for computer science")
    else:
        print("you are eligible for other groups")
 