#include<iostream>
using namespace std;


int board[3][3];



bool end_b()
{
	for(int i=0;i<3;i++) for(int j=0;j<3;j++) if(board[i][j]==3) return false;	
	return true;
}


int board_value()
{
    
    for (int row = 0; row<3; row++)
    {
        if (board[row][0]==board[row][1] &&
            board[row][1]==board[row][2])
        {
            if (board[row][0]==1)
                return +10;
            else if (board[row][0]==0)
                return -10;
        }
    }
   
    for (int col = 0; col<3; col++)
    {
        if (board[0][col]==board[1][col] &&
            board[1][col]==board[2][col])
        {
            if (board[0][col]==1)
                return +10;
  
            else if (board[0][col]==0)
                return -10;
        }
    }
  
    if (board[0][0]==board[1][1] && board[1][1]==board[2][2])
    {
        if (board[0][0]==1)
            return +10;
        else if (board[0][0]==0)
            return -10;
    }
  
    if (board[0][2]==board[1][1] && board[1][1]==board[2][0])
    {
        if (board[0][2]==1)
            return +10;
        else if (board[0][2]==0)
            return -10;
    }
  
    return 0;
}


int minimax(int depth,bool isMax)
{
    
    int value=board_value();
    if(value!=0)
    return value;
    if(end_b())
    return 0;
    
    
        if(isMax)
        {
            int b=-1000;
            for(int i=0;i<3;i++)
            {
                for(int j=0;j<3;j++)
                {
                if(board[i][j]==3)
                    {
                    board[i][j]=1;                    
                    b=max(minimax(depth+1,false),b);
					board[i][j]=3;
                    }
                }
            }
            return b;
        }
        else
        {

            int b=1000;
            for(int i=0;i<3;i++)
            {
                for(int j=0;j<3;j++)
                {
                if(board[i][j]==3)
                    {
                        board[i][j]=0;
                    b=min(minimax(depth+1,true),b);
						board[i][j]=3;
                    }
                }
            }
            return b;
        
        }
    

}

string winner()
{
	if(board_value()>0)
	return "computer wins";
	if(board_value()<0)
	return "you win";
	if(board_value()==0)
	return "tie";	
}

void bestmove()
{
	int b=-1000;
	pair<int,int>move;
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
			if(board[i][j]==3)
			{
				board[i][j]=1;
				int val=minimax(0,false);
				board[i][j]=3;
				if(val>b)
				{
					b=val;
					move=make_pair(i,j);
				}
			}	
		}
	}
	board[move.first][move.second]=1;
}

int main()
{
    for(int i=0;i<3;i++) for(int j=0;j<3;j++) board[i][j]=3;

    int k=0,x,y;
    
        
    while(!end_b() && board_value()==0)    
	{
	
	if(k%2==0)
       {
		 cout<<"your move: enter x,y \n";
            cin>>x>>y;
            board[x][y]=0;  
        
        for(int i=0;i<3;i++)
    	{
        for(int j=0;j<3;j++)
        cout<<board[i][j];
    	cout<<endl;
    	}
    }
    else
    {
		bestmove();
    	cout<<endl;
    	 for(int i=0;i<3;i++)
    	{
        for(int j=0;j<3;j++)
        cout<<board[i][j];
    	cout<<endl;
    	}
	}
	k++;
    	
	}
	cout<<"result :"<< winner();
	
}



