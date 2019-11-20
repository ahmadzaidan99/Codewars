#include<vector>

bool isValidWalk(std::vector<char> walk) {
  int nwalk = 0;
  int swalk = 0;
  int wwalk = 0;
  int ewalk = 0;
  
  if(walk.size()!=10)//if the walk isn't 10 mins just terminate
    return false;
  else{
    for (int i = 0; i < walk.size(); i++){//Count all the steps we are taking
      if(walk[i]=='n')
        nwalk++;
      if(walk[i]=='s')
        swalk++;
      if(walk[i]=='w')
        wwalk++;
      if(walk[i]=='e')
        ewalk++;
    }
}
  if(nwalk == swalk && wwalk == ewalk)//determining if we are back to the starting point
    return true;
  else
    return false;
}
