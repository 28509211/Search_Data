蒐集店家的評論

每個店家都會跑time.sleep(N) N秒 去蒐集評論， 這是為了防止google的反爬，而使城市無法繼續進行
過N秒後，會自動刪除該process，再重新開一個process執行下一個店家

可以修改__scroll_Review中的save_round: 每次滑的次數 * 10 == save_round 就把目前拿到的評論緩存
可以修改main.py的 sleep_times 用來控制 每個店家搜索評論要花多久時間

already_finded_store.txt: 已經找到得店家
read.txt: 要找評論的店家

review/ 資料夾內存店家的評論者和評論

執行main.py