import math

print("z score formula calculator, calculate any part of the z score formula as long as you have the other three parts")

def main():
    variable = input("calculate for 'z score', 'x', 'mean', or 'standard deviation'")
    print("for this next step, please separate each value with a space, keeping them in the same line")
    z_score = 0
    x = 0
    mean = 0
    standard_deviation = 0

    if variable == "z score":
        x, mean, standard_deviation = input("input the values of these variables in this order: x, mean, standard_deviation ").split()
        x = int(x)
        mean = int(mean)
        standard_deviation = int(standard_deviation)

        z_score = (x-mean)/standard_deviation

        z_score = str(z_score)
        x = str(x)
        mean = str(mean)
        standard_deviation = str(standard_deviation)
        print("your z score is " + z_score)
        print("other values used: " + x + " " + mean + " " + standard_deviation)

    elif variable == "x":
        z_score, mean, standard_deviation = input("input the values of these variables in this order: z score, mean, standard_deviation").split()
        z_score = int(z_score)
        mean = int(mean)
        standard_deviation = int(standard_deviation)

        x = mean + (z_score * standard_deviation)

        z_score = str(z_score)
        x = str(x)
        mean = str(mean)
        standard_deviation = str(standard_deviation)
        print("your x is " + x)
        print("other values used: " + z_score + " " + mean + " " + standard_deviation)

    elif variable == "mean":
        z_score, x, standard_deviation = input("input the values of these variables in this order: z score, x, standard_deviation").split()
        z_score = int(z_score)
        x = int(x)
        standard_deviation = int(standard_deviation)

        mean = x - (z_score * standard_deviation)

        z_score = str(z_score)
        x = str(x)
        mean = str(mean)
        standard_deviation = str(standard_deviation)
        print("your mean is " + mean)
        print("other values used: " + z_score + " " + x + " " + standard_deviation)

    elif variable == "standard deviation":
        z_score, x, mean = input("input the values of these variables in this order: z score, x, mean").split()
        z_score = int(z_score)
        x = int(x)
        mean = int(mean)

        standard_deviation = (x - mean) / z_score

        z_score = str(z_score)
        x = str(x)
        mean = str(mean)
        standard_deviation = str(standard_deviation)
        print("your standard deviation is " + standard_deviation)
        print("other values used: " + z_score + " " + x + " " + mean )

    else:
        print("use correct input ty")
        main()

    reset = input("would you like to calculate another value? ")
    if reset == "yes":
        main()
    else:
        print("ok goodbye")
        exit()

main()