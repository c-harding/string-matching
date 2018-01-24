class Compare
  @@cmps = 0

  def Compare.[](pattern, text, skip, i)
    puts text
    puts (' ' * skip + pattern)
    puts (' ' * (skip + i) + '^')
    @@cmps += 1
    text[skip + i] == pattern[i]
  end
  
  def Compare.count
    @@cmps
  end
end

def precalc pattern
  table = Hash.new(pattern.length)
  pattern[0...-1].each_char.with_index do |a,i|
    table[a] = pattern.length - i - 1
  end
  table
end

pattern = ARGV[0] or raise "No pattern"

text = ARGV[1] or raise "No text"

puts "Searching for \"#{pattern}\" in \"#{text}\""
puts

skip = 0

i = pattern.length - 1

table = precalc pattern
puts table

while skip + pattern.length < text.length
  while i >= 0 and Compare[pattern, text, skip, i]
    i -= 1
  end
  
  if i < 0
    puts "Match found at position #{skip}"
    i = pattern.length - 1
  end
  
  skip += table[text[skip + pattern.length - 1]]
end

puts "#{Compare.count} comparisons"
