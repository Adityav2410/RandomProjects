#include<iostream>
#include<cstdlib>
#include<bits/stdc++.h>

using namespace std;


class Vehicle{
	private:
	public:
		Vehicle(){
			// cout<<"Vehicle base class constructor invoked"<<endl;
		}
		void virtual printInfo() =0;
};

class Car:public Vehicle{

	private:
		string make;
		float mileeage , size;
	public:
		Car(){		// "AUdi 15mph, 5ft"
			cout<<"Car constructor invoked"<<endl;

			// stirng parsing
		}
		void printInfo(){
			cout<<"Car: print invoked"<<endl;
		}

};

class Truck:public Vehicle{
	private:
		string make;
		float mileage;
	public:
		Truck(){		// TATA 4mph
			cout<<"Truck constructor invoked"<<endl;
			// string parsing
		}
		void printInfo(){
			cout<<"Truck: print invoked"<<endl;
		}
};

unordered_map<string, function<Vehicle*()>> createMap(){
	unordered_map<string, function<Vehicle*()> > mp;
	// unordered_map<int, T > mp;
	mp["Car"] = [](){return new Car;};
	mp["Truck"] = [](){return new Truck;};
	return mp;
}


int main(){

	auto mp = createMap();
	auto obj_car = mp["Car"]();
	auto obj_truck = mp["Truck"]();
	// auto obj_truck = mp[1]();

	obj_car->printInfo();
	// obj_truck->printInfo();
}