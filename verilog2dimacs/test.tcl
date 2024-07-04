force N1 1'b0
force N2 1'b0
force N3 1'b0
force N6 1'b0
force N7 1'b0
run
lappend net_vals [value %b N23]
lappend net_vals [value %b N2]
lappend net_vals [value %b N19]
lappend net_vals [value %b N6]
lappend net_vals [value %b N10]
lappend net_vals [value %b N1]
lappend net_vals [value %b N11]
lappend net_vals [value %b N7]
lappend net_vals [value %b N3]
lappend net_vals [value %b N16]
lappend net_vals [value %b N22]
puts [open net_vals w] $net_vals
exit
