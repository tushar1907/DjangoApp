puts "Enter a number:"
num1 = gets.chomp()

#convert number to a floating point number
puts "Enter another number:"
num2 = gets.chomp().to_f

#to conver the number into integers to add them
puts (num1.to_i + num2)

#to conver the number into floating point numbers to add them
puts (num1.to_f + num2)