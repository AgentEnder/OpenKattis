# Counting Stars
## https://open.kattis.com/problems/countingstars

The field of astronomy has been significantly advanced through the use of computer technology. Algorithms can automatically survey digital images of the night sky, looking for new patterns.

For this problem, you should write such an analysis program which counts the number of stars visible in an bitmap image. An image consists of pixels, and each pixel is either black or white (represented by the characters # and -, respectively). All black pixels are considered to be part of the sky, and each white pixel is considered to be part of a star. White pixels that are adjacent vertically or horizontally are part of the same star.

Input
Each test case begins with a line containing a pair of integers 1≤m,n≤100. This is followed by m lines, each of which contains exactly n pixels. Input contains at least one and at most 50 test cases, and input ends at the end of file.

Output
For each case, display the case number followed by the number of stars that are visible in the corresponding image. Follow the format of the sample output.
