import Bio
from Bio.Seq import Seq
from Bio.Alphabet import Alphabet

my_seq = Seq("ATCGGACTTTAGGTG")
print("Seq %s is %i bases long" % (my_seq,len(my_seq)))
print("Reverse compliment is %s" % (my_seq.reverse_complement()))
print("Protein translation is %s" % (my_seq.translate()))