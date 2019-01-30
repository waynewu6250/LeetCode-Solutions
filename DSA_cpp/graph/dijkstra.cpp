//
// Created by 吳亭緯 on 2019-01-14.
//
#include <iostream>
#include <iomanip>
using namespace std;
#define SIZE   7
#define INFINITE 99999

int Graph_Matrix[SIZE][SIZE];
int distance[SIZE]={INFINITE};

void BuildGraph_Matrix(int *Path_Cost){

    int Start_Point;
    int End_Point;
    for(int i =1;i<SIZE;i++){
        for(int j=1;j<SIZE;j++){
            if(i==j) Graph_Matrix[i][j] = 0;
            else Graph_Matrix[i][j] = INFINITE;
        }
    }
    for(int i=0;i<SIZE;i++){
        Start_Point = Path_Cost[i*3];
        End_Point = Path_Cost[i*3+1];
        Graph_Matrix[Start_Point][End_Point]=Path_Cost[i*3+2];
    }

}

void printGraph_Matrix(){
    for(int i=1;i<SIZE;i++){
        cout << "vex" << i;
        for(int j=1;j<SIZE;j++){
            if(Graph_Matrix[i][j]==INFINITE)
                cout << setw(5) << 'x';
            else
                cout << setw(5) << Graph_Matrix[i][j];
        }
        cout << endl;
    }
}

void shortestPath(int vertex){
   extern int distance[SIZE];
   int shortest_vertex = 1;
   int shortest_distance;
   int has_run[SIZE]={0};

   //Get the first distances
   for(int i=0;i<SIZE;i++)
       distance[i] = Graph_Matrix[vertex][i];
   has_run[vertex] = 1;
   distance[vertex] = 0;


   for(int i=1; i<SIZE;i++){

       //Find the shortest distance
       shortest_distance = INFINITE;
       for(int j=1;j<SIZE-1;j++){
           if(has_run[j]==0 && shortest_distance>distance[j]){
               shortest_distance=distance[j];
               shortest_vertex=j;
           }
       }
       has_run[shortest_vertex] = 1;

       //Find the other distances
       for(int j=1;j<SIZE;j++){
           if(has_run[j]==0 && distance[j] > distance[shortest_vertex]+Graph_Matrix[shortest_vertex][j]){
               distance[j] = distance[shortest_vertex]+Graph_Matrix[shortest_vertex][j];
           }
       }

   }
}




int main(){

    extern int distance[SIZE];
    int data[10][3] = {{1,2,10}, {2,3,20},
                       {2,4,25}, {3,5,18},
                       {4,5,22}, {4,6,95},
                       {5,6,77}};

    BuildGraph_Matrix(&data[0][0]);
    cout << "Vertex vex1 vex2 vex3 vex4 vex5 vex6"<<endl;
    printGraph_Matrix();

    //Search the shortest path
    cout << endl << "Search the shortest path" << endl;
    cout << "Input the vertex you would like to search: ";
    int vertex;
    cin >> vertex;
    shortestPath(vertex);
    for (int j=1;j<SIZE;j++){
        cout << "Vertex " << vertex << " to " << setw(2) << j << " distance is " << setw(3) << distance[j] << endl;
    }
    cout << endl;
    return 0;


}