"""
Bob built a Web site and gave the URL only to his n friends, which he
numbered from 1 to n. He told friend number i that he/she can visit the
Web site at most i times. Now Bob has a counter, C, keeping track of the
total number of visits to the site (but not the identities of who visits).
What is the minimum value for C such that Bob can know that one of his
friends has visited his/her maximum allowed number of times?

At (n(n+1)/2)-n, everyone would be 1 off their maximum. Thus that +1 would
be the value of C where he would know someone has used all their visits.
"""