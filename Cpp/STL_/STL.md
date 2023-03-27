<center>

## The STL.md is learn from "侯捷"

## STL六大部件 (Components)
### 1. 容器 conrainers
### 2. 分配器 allocators
### 3. 算法  algorithms
### 4. 迭代器 iterators
### 5. 适配器 adpters
### 6. 仿函式 functors
</center>


~~~ 

#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>


int main(){
	vector<int,allocator<int>> v(ia,ia+6);
	//vector is the container
	//and the allocator mostly do not must be written

	cout<<count_if(v.begin(),v.end(),notl(bind2nd(less<int>(),40)));
	//the "count_if" is the algorithm
	//the "v.begin(),v.end()" are iterators 
	//the "notl()" is a function adapter(negator) 
	//the "bind2nd" is a function adapter(binder)
 	//the "less<int>()" is a function object

	return 0;
}
~~~


``` 
std::vector <double> vec
for (auto elem : vec ){
	//auto 据右推左
	std::cout<<elem<<std::endl;
} 
```



