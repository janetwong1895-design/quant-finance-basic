# 第8章：資料與交易執行約定

原創人工合成資料，建立於31 October 2026；沒有市場資料流或真實公司行動。日期為依序排列的假設交易日，刻意包含週末。採儲存庫MIT授權。價格單位新臺幣／單位，皆為有限正值；是未調整的合成價格，不含股票分割、配息、違約或其他公司行動。

`date`：不重複、依時序排列的ISO交易日期。`open`：該日開盤時可得的價格。`close`：該日收盤後才可得的價格。

開發資料Jan2–17,2025。已公開的遷移資料Feb3–12,2025。兩者都不證明市場獲利能力，也不是保密保留資料。全部資料可查看；不得調參、最佳化參數或選擇性刪除試驗。

固定規則：包含t的最近3筆收盤價平均。嚴格close[t]>mean時目標1，否則0。收盤t後訊號於open[t+1]執行，賺取open[t+1]→open[t+2]報酬率。前3筆收盤價作暖身；不使用不完整的最後區間。`backtest(data,{costBps=10,initial=1000,window=3})`驗證日期不重複且依序、價格正值、視窗只允許3、成本0–100bps。回傳逐列資料、最終策略／基準資產、小數總報酬率、最後出場成本與起始／成本／視窗中繼資料。匯出DEVELOPMENT_DATA=DATA；EVALUATION_DATA=TRANSFER_DATA；EVALUATION_ID='qf-synthetic-feb2025-v1'只是已公開的教學標籤。第9章使用另一個已揭露條件的評估案例。

逐列欄位：signalDate、entryDate、exitDate、close、average、position、previousPosition、turnover=abs(position−previous)、grossReturn=nextopen/entryopen−1、costRate=(costBps/10000)*turnover、startWealth、endWealth、benchmarkStart、benchmarkEnd。報酬率為小數，資產為新臺幣。初始先前權重0；資產先乘成本因子，再乘1+position*grossReturn。最後持有部位以1−c*lastWeight扣費平倉。因此紀錄最後一列尚未計最後平倉。基準同為起始1000，從第一個可交易開盤持有至相同最後開盤，按相同c付進場與最後出場費，中間不交易。開發可交易開盤區間Jan5→Jan17；遷移區間Feb6→Feb12。現金報酬率零；無槓桿、放空、利息、配息、稅、違約或額外買賣價差／衝擊／滑價。固定0/1權重不涉及中間權重漂移。

保留每次成本敏感度。擾動未來價格不得改變先前部位。固定路徑提高費率，不能改善最終資產。這些測試只偵測特定錯誤，不證明沒有其他實作缺陷。
