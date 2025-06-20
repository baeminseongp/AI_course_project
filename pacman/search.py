# -*- coding: utf-8 -*-

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Queue
from util import Stack



class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    fringe = Stack()  # DFS는 Stack 사용
    visited = set()   # 방문한 노드 저장
    start = problem.getStartState()
    fringe.push((start, []))  # (현재 상태, 경로)

    while not fringe.isEmpty():
        state, path = fringe.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.add(state)
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in visited:
                    fringe.push((successor, path + [action]))

    return []  # 실패 시 빈 리스트 반환

def breadthFirstSearch(problem):
    fringe = Queue()  # BFS는 Queue 사용
    visited = set()   # 방문한 상태 기억
    start = problem.getStartState()
    fringe.push((start, []))  # (현재 상태, 경로)

    while not fringe.isEmpty():
        state, path = fringe.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.add(state)
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in visited:
                    fringe.push((successor, path + [action]))

    return []  # 실패 시 빈 리스트 반환

def uniformCostSearch(problem):
    from util import PriorityQueue

    fringe = PriorityQueue()  # 우선순위 큐 사용
    visited = set()
    start = problem.getStartState()
    
    # 우선순위 큐에는 (state, path, total_cost)를 넣고, total_cost를 기준으로 우선순위 지정
    fringe.push((start, [], 0), 0)

    while not fringe.isEmpty():
        state, path, cost = fringe.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.add(state)
            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in visited:
                    new_cost = cost + step_cost
                    fringe.push((successor, path + [action], new_cost), new_cost)

    return []  # 실패 시

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
