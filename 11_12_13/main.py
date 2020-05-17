import pandas as pd
import numpy as np
class Agent:
    def __init__(self, env, freq=30, data, tickers,  portfolio):
        """
        params :
            data : 전체 유니버스 가격 데이터

        AGENT : 돈 얼마 가지고 있는지, 종목 비중을 어떻게 할지, 투자 기간을 얼마나 할지.
        money : 자산(백분율)
        tickers : 스크리닝된 종목들의 종목코드
        w : 각 자산의 비중 벡터, agent내부의 메소드를 통해서 구한다.
        freq : 리밸런싱 주기.
        log : 리밸런싱할때마다 투자자의 자산의 비중 추이(나중에 비중그래프랑 수익률 그래프 만들때 씁니다.) 결과 도출하기전에 self.log['sum'] = self.log.sum(axis=1)
        portfolio : 포트폴리오의 각 자산 비중을 결정하는 방법. EW - 동일비중 / MV - 최소분산 / DR - 최대분산효과 / ERC - 위험균형 / IDX = 인덱스
        covmat = 공분산행렬
        """
        self.env = env
        self.money = 1
        self.tickers = tickers
        self.w = None        
        self.freq = freq
        self.log = pd.DataFrame(0, index=data.index, columns=data.columns)
        self.portfolio = portfolio
        self.covmat = None

    def w값과 money값을 참조중인 env에 전달하고, env는 전달받은 값을 통해서 투자 결과를 계산하고, 로그와 money(로그의 마지막 행의 Sum값)를 반환한다.
        w계산하는 메소드()
        result = self.env.w값 받고 계산해서 로그 데이터프레임 리턴하는 메소드(w, money)
        self.log의 tp-freq : tp 행을 result값으로 치환한다. 그리고 result값의 마지막 row sum을 money에 update.

    def w 계산하는 메소드.

class Environment:
    """
    Environment : 현재 투자시점이 어디쯤인지, 그 투자시점에서 데이터들의 수익률은 얼마나 되는지.
    
    
    """
    def __init__(self, agent, data, tickers):
        """
        data : pd.DataFrame

        """
        self.agent = agent
        self.dataframe = data
        self.dataframe = sefl.dataframe.pct_change(1) + 1
        self.dataframe = self.dataframe.iloc[1:]
        self.selectedData = self.dataframe[tickers]
        
        self.tp = agent.freq

    def setTickers(tickers):
        self.selectedData = self.dataframe[tickers]
    

    def gen_covmat_to_Agent():#3
        """
        (tp - freq, tp)시점의 데이터를 통해 공분산 행렬을 생성하고, 참조된 agent에 전달한다.
        """
        freq = self.agent.freq
        n = len(tickers)
        covmat = np.identity(n)
        
        handledData = dataframe.iloc[tp - freq : tp]
        
        for i in range(n):
            for j in range(n):
                covmat[i,j] = np.cov(handledData[:,i],handledData[:,j])[0,1]
        self.agent.covmat = covmat
        
    def w값받고 계산하는 메소드(agent 내부에서 호출됨):
        return 로그 데이터프레임
        
class Visualizer:
    agent로부터 투자 로그를 받아와서 결과 정리.


if __name__ == "__main__":
    pass