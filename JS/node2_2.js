let x = +prompt('input num');
if (x < -6){
	var y = 1-x;
}
else if (-6 <= x && x <= -4){
	var y = (x-1)/4;
}
else if (x > -4){
	var y = 2*x - 5;
}
alert(y);