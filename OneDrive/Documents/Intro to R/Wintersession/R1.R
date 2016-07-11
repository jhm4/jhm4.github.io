my_variable <- 2
my_variable

rm(my_variable)


v <- c(2, 5, 10, 12)
v
1:5
1:10
length(v)
mean(v)
var(v)
median(v)
sum(v)
range(v)
min(v)
summary(v)
sort(v, decreasing = TRUE)

v[-3]
v2 <- v[-(2:3)]
v + 1
v / 2

ch <- c("hello", "world")
ch[2]
#stringr package
# can't/shouldn't do:
#mixed <- c("hello", 1, "world", 2)

v3 <- c(20, 25, 11, 4)
c(v, v3)

gender <- factor(c("male", "female", "female", "female", "male"))
gender

2 > 5
x <- 6
x == 6
