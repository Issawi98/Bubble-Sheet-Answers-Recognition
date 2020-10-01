def getAnswers(centroids):
    # setting defaults
    gender = ["Not Solved", 0]
    semester = ["Not Solved", 0]
    program = ["Not Solved", 0]
    firstQ = [["Not Solved", 0], ["Not Solved", 0], ["Not Solved", 0], ["Not Solved", 0], ["Not Solved", 0]]
    secondQ = [["Not Solved", 0], ["Not Solved", 0], ["Not Solved", 0], ["Not Solved", 0], ["Not Solved", 0],
              ["Not Solved", 0]]
    thirdQ = [["Not Solved", 0], ["Not Solved", 0], ["Not Solved", 0]]
    fourthQ = [["Not Solved", 0], ["Not Solved", 0], ["Not Solved", 0]]
    fifthQ = [["Not Solved", 0], ["Not Solved", 0]]

    # getting exact values, check for invalid answers.
    for i, j in centroids[1:]:
        # print( str(i) + "," + str(j))
        if 85 < j < 95:
            if 370 < i < 385:
                gender[0] = "Male"
                gender[1] += 1
            elif 410 < i < 425:
                gender[0] = "Female"
                gender[1] += 1
            if gender[1] > 1:
                gender[0] = "Invalid Answer"

        elif 108 < j < 115:
            if 160 < i < 175:
                semester[0] = "Fall"
                semester[1] += 1
            elif 243 < i < 250:
                semester[0] = "Spring"
                semester[1] += 1
            elif 323 < i < 330:
                semester[0] = "Summer"
                semester[1] += 1
            if semester[1] > 1:
                semester[0] = "Invalid Answer"

        elif 134 < j < 139:
            if 134 < i < 142:
                program[0] = "MCTA"
                program[1] += 1
            elif 174 < i < 180:
                program[0] = "ENVER"
                program[1] += 1
            elif 213 < i < 219:
                program[0] = "BLDG"
                program[1] += 1
            elif 255 < i < 260:
                program[0] = "CESS"
                program[1] += 1
            elif 293 < i < 300:
                program[0] = "ERGY"
                program[1] += 1
            elif 335 < i < 340:
                program[0] = "COMM"
                program[1] += 1
            elif 370 < i < 389:
                program[0] = "MANF"
                program[1] += 1

        elif 144 < j < 152:
            if 134 < i < 142:
                program[0] = "LAAR"
                program[1] += 1
            elif 173 < i < 180:
                program[0] = "MATL"
                program[1] += 1
            elif 213 < i < 219:
                program[0] = "CISE"
                program[1] += 1
            elif 253 < i < 260:
                program[0] = "HAUD"
                program[1] += 1
            if program[1] > 1:
                program[0] = "Invalid Answer"

        elif 290 < j < 295:
            if 330 < i < 342:
                firstQ[0][0] = "Strongly Agree"
                firstQ[0][1] += 1
            elif 360 < i < 372:
                firstQ[0][0] = "Agree"
                firstQ[0][1] += 1
            elif 390 < i < 402:
                firstQ[0][0] = "Neutral"
                firstQ[0][1] += 1
            elif 420 < i < 432:
                firstQ[0][0] = "Disagree"
                firstQ[0][1] += 1
            elif 450 < i < 462:
                firstQ[0][0] = "Strongly Disagree"
                firstQ[0][1] += 1
            if firstQ[0][1] > 1:
                firstQ[0][0] = "Invalid Answer"

        elif 300 < j < 310:
            if 330 < i < 340:
                firstQ[1][0] = "Strongly Agree"
                firstQ[1][1] += 1
            elif 360 < i < 372:
                firstQ[1][0] = "Agree"
                firstQ[1][1] += 1
            elif 390 < i < 402:
                firstQ[1][0] = "Neutral"
                firstQ[1][1] += 1
            elif 420 < i < 432:
                firstQ[1][0] = "Disagree"
                firstQ[1][1] += 1
            elif 450 < i < 462:
                firstQ[1][0] = "Strongly Disagree"
                firstQ[1][1] += 1
            if firstQ[1][1] > 1:
                firstQ[1][0] = "Invalid Answer"

        elif 313 < j < 321:
            if 330 < i < 342:
                firstQ[2][0] = "Strongly Agree"
                firstQ[2][1] += 1
            elif 360 < i < 372:
                firstQ[2][0] = "Agree"
                firstQ[2][1] += 1
            elif 390 < i < 402:
                firstQ[2][0] = "Neutral"
                firstQ[2][1] += 1
            elif 420 < i < 432:
                firstQ[2][0] = "Disagree"
                firstQ[2][1] += 1
            elif 450 < i < 462:
                firstQ[2][0] = "Strongly Disagree"
                firstQ[2][1] += 1
            if firstQ[2][1] > 1:
                firstQ[2][0] = "Invalid Answer"

        elif 326 < j < 335:
            if 330 < i < 340:
                firstQ[3][0] = "Strongly Agree"
                firstQ[3][1] += 1
            elif 360 < i < 372:
                firstQ[3][0] = "Agree"
                firstQ[3][1] += 1
            elif 390 < i < 402:
                firstQ[3][0] = "Neutral"
                firstQ[3][1] += 1
            elif 420 < i < 432:
                firstQ[3][0] = "Disagree"
                firstQ[3][1] += 1
            elif 450 < i < 462:
                firstQ[3][0] = "Strongly Disagree"
                firstQ[3][1] += 1
            if firstQ[3][1] > 1:
                firstQ[3][0] = "Invalid Answer"

        elif 338 < j < 348:
            if 330 < i < 342:
                firstQ[4][0] = "Strongly Agree"
                firstQ[4][1] += 1
            elif 360 < i < 372:
                firstQ[4][0] = "Agree"
                firstQ[4][1] += 1
            elif 390 < i < 402:
                firstQ[4][0] = "Neutral"
                firstQ[4][1] += 1
            elif 420 < i < 432:
                firstQ[4][0] = "Disagree"
                firstQ[4][1] += 1
            elif 450 < i < 462:
                firstQ[4][0] = "Strongly Disagree"
                firstQ[4][1] += 1
            if firstQ[4][1] > 1:
                firstQ[4][0] = "Invalid Answer"

        elif 373 < j < 383:
            if 330 < i < 342:
                secondQ[0][0] = "Strongly Agree"
                secondQ[0][1] += 1
            elif 360 < i < 372:
                secondQ[0][0] = "Agree"
                secondQ[0][1] += 1
            elif 390 < i < 402:
                secondQ[0][0] = "Neutral"
                secondQ[0][1] += 1
            elif 420 < i < 432:
                secondQ[0][0] = "Disagree"
                secondQ[0][1] += 1
            elif 450 < i < 462:
                secondQ[0][0] = "Strongly Disagree"
                secondQ[0][1] += 1
            if secondQ[0][1] > 1:
                secondQ[0][0] = "Invalid Answer"

        elif 386 < j < 392:
            if 330 < i < 342:
                secondQ[1][0] = "Strongly Agree"
                secondQ[1][1] += 1
            elif 360 < i < 372:
                secondQ[1][0] = "Agree"
                secondQ[1][1] += 1
            elif 390 < i < 402:
                secondQ[1][0] = "Neutral"
                secondQ[1][1] += 1
            elif 420 < i < 432:
                secondQ[1][0] = "Disagree"
                secondQ[1][1] += 1
            elif 450 < i < 462:
                secondQ[1][0] = "Strongly Disagree"
                secondQ[1][1] += 1
            if secondQ[1][1] > 1:
                secondQ[1][0] = "Invalid Answer"

        elif 397 < j < 403:
            if 330 < i < 342:
                secondQ[2][0] = "Strongly Agree"
                secondQ[2][1] += 1
            elif 360 < i < 372:
                secondQ[2][0] = "Agree"
                secondQ[2][1] += 1
            elif 390 < i < 402:
                secondQ[2][0] = "Neutral"
                secondQ[2][1] += 1
            elif 420 < i < 432:
                secondQ[2][0] = "Disagree"
                secondQ[2][1] += 1
            elif 450 < i < 462:
                secondQ[2][0] = "Strongly Disagree"
                secondQ[2][1] += 1
            if secondQ[2][1] > 1:
                secondQ[2][0] = "Invalid Answer"

        elif 407 < j < 416:
            if 330 < i < 342:
                secondQ[3][0] = "Strongly Agree"
                secondQ[3][1] += 1
            elif 360 < i < 372:
                secondQ[3][0] = "Agree"
                secondQ[3][1] += 1
            elif 390 < i < 402:
                secondQ[3][0] = "Neutral"
                secondQ[3][1] += 1
            elif 420 < i < 432:
                secondQ[3][0] = "Disagree"
                secondQ[3][1] += 1
            elif 450 < i < 462:
                secondQ[3][0] = "Strongly Disagree"
                secondQ[3][1] += 1
            if secondQ[3][1] > 1:
                secondQ[3][0] = "Invalid Answer"

        elif 420 < j < 428:
            if 330 < i < 342:
                secondQ[4][0] = "Strongly Agree"
                secondQ[4][1] += 1
            elif 360 < i < 372:
                secondQ[4][0] = "Agree"
                secondQ[4][1] += 1
            elif 390 < i < 402:
                secondQ[4][0] = "Neutral"
                secondQ[4][1] += 1
            elif 420 < i < 432:
                secondQ[4][0] = "Disagree"
                secondQ[4][1] += 1
            elif 450 < i < 462:
                secondQ[4][0] = "Strongly Disagree"
                secondQ[4][1] += 1
            if secondQ[4][1] > 1:
                secondQ[4][0] = "Invalid Answer"

        elif 431 < j < 440:
            if 330 < i < 342:
                secondQ[5][0] = "Strongly Agree"
                secondQ[5][1] += 1
            elif 360 < i < 372:
                secondQ[5][0] = "Agree"
                secondQ[5][1] += 1
            elif 390 < i < 402:
                secondQ[5][0] = "Neutral"
                secondQ[5][1] += 1
            elif 420 < i < 432:
                secondQ[5][0] = "Disagree"
                secondQ[5][1] += 1
            elif 450 < i < 462:
                secondQ[5][0] = "Strongly Disagree"
                secondQ[5][1] += 1
            if secondQ[5][1] > 1:
                secondQ[5][0] = "Invalid Answer"

        elif 468 < j < 475:
            if 330 < i < 342:
                thirdQ[0][0] = "Strongly Agree"
                thirdQ[0][1] += 1
            elif 360 < i < 372:
                thirdQ[0][0] = "Agree"
                thirdQ[0][1] += 1
            elif 390 < i < 402:
                thirdQ[0][0] = "Neutral"
                thirdQ[0][1] += 1
            elif 420 < i < 432:
                thirdQ[0][0] = "Disagree"
                thirdQ[0][1] += 1
            elif 450 < i < 462:
                thirdQ[0][0] = "Strongly Disagree"
                thirdQ[0][1] += 1
            if thirdQ[0][1] > 1:
                thirdQ[0][0] = "Invalid Answer"

        elif 480 < j < 489:
            if 330 < i < 342:
                thirdQ[1][0] = "Strongly Agree"
                thirdQ[1][1] += 1
            elif 360 < i < 372:
                thirdQ[1][0] = "Agree"
                thirdQ[1][1] += 1
            elif 390 < i < 402:
                thirdQ[1][0] = "Neutral"
                thirdQ[1][1] += 1
            elif 420 < i < 432:
                thirdQ[1][0] = "Disagree"
                thirdQ[1][1] += 1
            elif 450 < i < 462:
                thirdQ[1][0] = "Strongly Disagree"
                thirdQ[1][1] += 1
            if thirdQ[1][1] > 1:
                thirdQ[1][0] = "Invalid Answer"

        elif 492 < j < 500:
            if 330 < i < 342:
                thirdQ[2][0] = "Strongly Agree"
                thirdQ[2][1] += 1
            elif 360 < i < 372:
                thirdQ[2][0] = "Agree"
                thirdQ[2][1] += 1
            elif 390 < i < 402:
                thirdQ[2][0] = "Neutral"
                thirdQ[2][1] += 1
            elif 420 < i < 432:
                thirdQ[2][0] = "Disagree"
                thirdQ[2][1] += 1
            elif 450 < i < 462:
                thirdQ[2][0] = "Strongly Disagree"
                thirdQ[2][1] += 1
            if thirdQ[2][1] > 1:
                thirdQ[2][0] = "Invalid Answer"

        elif 528 < j < 536:
            if 330 < i < 342:
                fourthQ[0][0] = "Strongly Agree"
                fourthQ[0][1] += 1
            elif 360 < i < 372:
                fourthQ[0][0] = "Agree"
                fourthQ[0][1] += 1
            elif 390 < i < 402:
                fourthQ[0][0] = "Neutral"
                fourthQ[0][1] += 1
            elif 420 < i < 432:
                fourthQ[0][0] = "Disagree"
                fourthQ[0][1] += 1
            elif 450 < i < 462:
                fourthQ[0][0] = "Strongly Disagree"
                fourthQ[0][1] += 1
            if fourthQ[0][1] > 1:
                fourthQ[0][0] = "Invalid Answer"

        elif 539 < j < 548:
            if 330 < i < 342:
                fourthQ[1][0] = "Strongly Agree"
                fourthQ[1][1] += 1
            elif 360 < i < 372:
                fourthQ[1][0] = "Agree"
                fourthQ[1][1] += 1
            elif 390 < i < 402:
                fourthQ[1][0] = "Neutral"
                fourthQ[1][1] += 1
            elif 420 < i < 432:
                fourthQ[1][0] = "Disagree"
                fourthQ[1][1] += 1
            elif 450 < i < 462:
                fourthQ[1][0] = "Strongly Disagree"
                fourthQ[1][1] += 1
            if fourthQ[1][1] > 1:
                fourthQ[1][0] = "Invalid Answer"

        elif 564 < j < 574:
            if 330 < i < 342:
                fourthQ[2][0] = "Strongly Agree"
                fourthQ[2][1] += 1
            elif 360 < i < 372:
                fourthQ[2][0] = "Agree"
                fourthQ[2][1] += 1
            elif 390 < i < 402:
                fourthQ[2][0] = "Neutral"
                fourthQ[2][1] += 1
            elif 420 < i < 432:
                fourthQ[2][0] = "Disagree"
                fourthQ[2][1] += 1
            elif 450 < i < 462:
                fourthQ[2][0] = "Strongly Disagree"
                fourthQ[2][1] += 1
            if fourthQ[2][1] > 1:
                fourthQ[2][0] = "Invalid Answer"

        elif 598 < j < 608:
            if 330 < i < 342:
                fifthQ[0][0] = "Strongly Agree"
                fifthQ[0][1] += 1
            elif 360 < i < 372:
                fifthQ[0][0] = "Agree"
                fifthQ[0][1] += 1
            elif 390 < i < 402:
                fifthQ[0][0] = "Neutral"
                fifthQ[0][1] += 1
            elif 420 < i < 432:
                fifthQ[0][0] = "Disagree"
                fifthQ[0][1] += 1
            elif 450 < i < 462:
                fifthQ[0][0] = "Strongly Disagree"
                fifthQ[0][1] += 1
            if fifthQ[0][1] > 1:
                fifthQ[0][0] = "Invalid Answer"

        elif 611 < j < 620:
            if 330 < i < 342:
                fifthQ[1][0] = "Strongly Agree"
                fifthQ[1][1] += 1
            elif 360 < i < 372:
                fifthQ[1][0] = "Agree"
                fifthQ[1][1] += 1
            elif 390 < i < 402:
                fifthQ[1][0] = "Neutral"
                fifthQ[1][1] += 1
            elif 420 < i < 432:
                fifthQ[1][0] = "Disagree"
                fifthQ[1][1] += 1
            elif 450 < i < 462:
                fifthQ[1][0] = "Strongly Disagree"
                fifthQ[1][1] += 1
            if fifthQ[1][1] > 1:
                fifthQ[1][0] = "Invalid Answer"

    return gender, semester, program, firstQ, secondQ, thirdQ, fourthQ, fifthQ