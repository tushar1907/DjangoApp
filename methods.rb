def sayHi(name= "Default", age=-1)
    puts "Say Hi to " + name + " and age is " + age.to_s
end


puts "Enter the name: "
name = gets.chomp()
puts sayHi(name)