class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        def get_cycle(m_min, m_max, n_min, n_max):
            print(m_min, m_max, n_min, n_max)
            if m_min>m_max or n_min>n_max:
                return
            
            if m_min==m_max:
                for j in range(n_min,n_max+1):
                    res.append(
                        matrix[m_min][j]
                    )
                return
            if n_min==n_max:
                for i in range(m_min, m_max+1):
                    res.append(
                        matrix[i][n_min]
                    )
                return
            
            for j in range(n_min,n_max):
                res.append(
                    matrix[m_min][j]
                )
            for i in range(m_min,m_max):
                res.append(
                    matrix[i][n_max]
                )
            for j in range(n_max,n_min,-1):
                res.append(
                    matrix[m_max][j]
                )
            for i in range(m_max,m_min,-1):
                res.append(
                    matrix[i][n_min]
                )

            get_cycle(m_min+1, m_max-1, n_min+1, n_max-1)
        
        get_cycle(0,len(matrix)-1,0,len(matrix[0])-1)
        return res