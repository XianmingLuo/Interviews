#include <assert.h>

#include <cstdlib>
#include <iostream>
//MyArray class is used as a container that does not need to initialize the memory
//It also promises O(1)(not amortized) get and set
//Precondition: all the value to store should be non-negative integer
class MyArray {
 private:
  int * array;
  int * traceArray;
  int * hashArray;
  int length;
  int traceLen;

 public:
  MyArray(size_t l) {
    length = l;
    traceLen = 0;
    array = new int[length];
    traceArray = new int[length];
    hashArray = new int[length];
  }
  //Get the value of the specified index of the array
  //If the specified index holds garbage, return -1
  //If the specified index holds meaningful value, return the value
  int get(int index) {
    if (index >= length) {
      //throw exception
      throw std::out_of_range("Index is out of range.");
    }
    int traceIdx = hashArray[index];
    //garbage found in hashArray
    if (traceIdx >= traceLen) {
      return -1;
    }
    //garbage found in hashArray
    if (traceArray[traceIdx] != index) {
      return -1;
    }
    return array[index];
  }
  //Assign the value to the index of array
  //Update traceArray and hashArray
  void set(int index, int value) {
    if (index >= length) {
      //throw exception
      throw std::out_of_range("Index is out of range.");
    }
    //update traceArray and hashArray only when the index holds garbage
    //or will have duplicates
    if (get(index) == -1) {
      traceArray[traceLen] = index;
      hashArray[index] = traceLen;
      traceLen += 1;
    }
    array[index] = value;
  }
  ~MyArray() {
    delete[] array;
    delete[] traceArray;
    delete[] hashArray;
  }
};

int main() {
  MyArray array(1000);
  for (int i = 0; i < 1000; i++) {
    assert(array.get(i) == -1);
  }
  for (int i = 0; i < 1000; i++) {
    if (i % 2 == 0) {
      array.set(i, i - 1);
    }
  }
  for (int i = 0; i < 1000; i++) {
    if (i % 2 == 0) {
      assert(array.get(i) == (i - 1));
    }
    else {
      assert(array.get(i) == -1);
    }
  }
  return EXIT_SUCCESS;
}
