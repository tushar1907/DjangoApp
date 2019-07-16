name = "Mike"
lastname = "   Gupta"

puts name

first = nil


#puts is used to print something in new line
puts first
puts name
puts lastname

#String methods

#convert string to upper case
puts "String in upcase " + name.upcase()

#convert string to lower case
puts name.downcase()

#used to strip white spaces from front and back
puts lastname.strip()

#count the length of the char
puts name.length()

#to check if current char or phrase present in the string
puts name.include? "ik"

#get the char in the string from index or from index range
puts name[3]
puts name[0,2]

#get where the index starts from the char in the string
puts name.index("ike")

#can also be used on string live
puts "Tushar".upcase