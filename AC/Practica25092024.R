data <- data.frame("x1"=c(
  2.771244718,
  1.728571309,
  3.678319846,
  3.961043357,
  2.999208922,
  7.497545867,
  9.00220326,
  7.444542326,
  10.12493903,
  6.642287351
),
"x2"=c(
  1.784783929,
  1.169761413,
  2.81281357,
  2.61995032,
  2.209014212,
  3.162953546,
  3.339047188,
  0.476683375,
  3.234550982,
  3.319983761
),

"y"=c(
  0,
  0,
  0,
  0,
  0,
  1,
  1,
  1,
  1,
  1
))

qq = data[order(data$x1),]

for (x in qq){
  print(x)
}

for (i in 2:nrow(qq) -1){
  print(qq[1])
}