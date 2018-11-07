#For the S2 calculation, want all bundles within a radius of 1.6
package require pbctools

#set start [lindex $argv 0]
#set stride [lindex $argv 1]
#set stop [lindex $argv 2]
set start 2
set stride 1
set stop -1

#initialize arrays for each of the data sets we're generating
#set g_unit {}
set n_samples 0
 
#set the key parameters for doing atom selections
set L [lindex [lindex [pbc get] 0] 0]
set N [ [atomselect top "all"] num]
set n_frames [molinfo top get numframes] 
set A [atomselect top "type A"]
set C [atomselect top "type C"]
set AA [measure gofr $A $A usepbc 1 first $start last $stop step $stride]
set CC [measure gofr $C $C usepbc 1 first $start last $stop step $stride]

puts "outputting data"
set file [open "gofrAA.txt" w]
puts $file "# r gAA"
set r [lindex $AA 0 ]
set g [lindex $AA 1]
for {set i 0} {$i < [llength $r] } {incr i} {
    set values [list [lindex $r $i] [lindex $g $i]]
    puts $file $values
}
close $file
set file [open "gofrCC.txt" w]
puts $file "# r gCC"
set r [lindex $CC 0 ]
set g [lindex $CC 1]
for {set i 0} {$i < [llength $r] } {incr i} {
    set values [list [lindex $r $i] [lindex $g $i]]
    puts $file $values
}
close $file

exit
