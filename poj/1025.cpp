#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <stack>
#include <utility>
#include <queue>
using namespace std;
typedef map<int, int> Schedule;

int strtime_to_int(string strTime)
{
	int hour, minute, sec;
	sscanf_s(strTime.c_str(), "%d:%d:%d", &hour, &minute, &sec);
	return hour * 3600 + minute * 60 + sec;
}

string inttime_to_str(int intTime)
{
	char ret[20];
	int hour = intTime / 3600, minute = (intTime % 3600) / 60, sec = intTime % 60;
	sprintf_s(ret, "%.2d:%.2d:%.2d", hour, minute, sec);
	return string(ret);
}

class Agent
{
public:
	static int gBeginTime;
	char mCode = ' ';
	int mEnterTime = 0;
	Schedule mSch = {};

	Agent(char code, int enterTime, Schedule sch): mCode(code), mEnterTime(enterTime), mSch(sch)
	{
	}

	Agent()
	{
		reset();
	}

	void reset()
	{
		mCode = ' ';
		mEnterTime = 0;
		mSch = {};
	}
};

bool operator >>(istream& ins, Agent& a)
{
	a.reset();
	if (!(ins >> a.mCode) || a.mCode == '.')
	{
		return false;
	}
	string sTime;
	if (!(ins >> sTime))
	{
		return false;
	}
	a.mEnterTime = strtime_to_int(sTime);
	if(a.mEnterTime<Agent::gBeginTime)
	{
		Agent::gBeginTime = a.mEnterTime;
	}
	int house, secs;
	while (ins >> house && house)
	{
		ins >> secs;
		a.mSch[house] = secs;
	}
	return true;
}

int Agent::gBeginTime = INT32_MAX;

int main()
{
	vector<Agent> agents;
	while (true)
	{
		Agent tmp;
		if (cin >> tmp)
		{
			agents.push_back(tmp);
		}
		else
		{
			break;
		}
	}
	return 0;
}
