#!/usr/bin/env ruby
#ruby script to hat accepts one argument and pass it to a regular expression

puts ARGV[0].scan(/School/).join
