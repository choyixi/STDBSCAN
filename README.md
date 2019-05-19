# STDBSCAN
##An implementation of Spatio-temporal DBSCAN algorithm in Python. 
The algorithm was developed by Birant, D., & Kut, A.:

<code>[Birant, D., & Kut, A. (2007). ST-DBSCAN: An algorithm for clustering spatial-temporal data. Data Knowl. Eng., 60, 208-221.](https://pdf.sciencedirectassets.com/271546/1-s2.0-S0169023X06X01829/1-s2.0-S0169023X06000218/main.pdf?x-amz-security-token=AgoJb3JpZ2luX2VjEFwaCXVzLWVhc3QtMSJGMEQCIDrzVFMqtiviTg9r2hXEVIxiWf%2FqY3uuV%2F%2BGT8zEPLI%2BAiBO103a6wIJxVh0uTsNfXUssp6WRSsSQSdnI%2B2bFs%2B6XSraAwhkEAIaDDA1OTAwMzU0Njg2NSIMICOTnzIFHvbCNZJSKrcDEiSGGqlbx%2B0VZRZvtAL%2B2TgvU4xaoOrj6pOpzYZ%2FiU2hc1V3LwPWHDHym8jSPdBXlvmjxrvIh%2FfpijYJjZAckTApdWYVsFGoVd13SJOFEqKn4JvvAt6l8TEl%2BwL7z6dRWraSIaW03YFiCZRcHPXuOZ7Z2IQGBuV1ORolXeQPeHoE5NjsyreoXFxwzEHv0cc21iM9idEtjNHaTD4RNAKMgAQXRufqfkADheyln0Mx0RH9u2fYJjBNlvYesyt5jjebX%2FGL1odzaXeR6VMM67HwRvrvEPYmQG1e9WcyM25hhiQiboEvay2yF9tYYOdb5smJttXOvA8qpebpxRAsyhbpDwgHgXzJrOkpnmqdF2PFv9Pzyy%2BYM55INTt9i%2FnMR7Tp8NsxSMZpj7MrEFHKfS0o6L0gmWrYcr9XiRntA3Ij2YRmlfROZ3fteDGlmLQibULo0Xwqx%2BFZu%2FXG2YGAF1tjMlKMT%2BgU6g9f2OBWTw3kmiNbsqkFmLYKhib%2BuVYtvw1AcezkubNbnoUNTppFfic%2F6%2BD%2B7%2BPDCyu4WHoIK%2BgAwJceq35m4hccXe6i%2FX1kFbzg9vNzP%2BctbzCt2IbnBTq1AdWVzjh%2BPEkN7USq3Dkz7FQmNshFa8l5wq%2BLSssbdAmdbrwDFzgBlDnUC8I9CZlv6B6QxSReWT9HDq8EL36YI8MEVwn%2FFoKtfZaj98oAjsU0Ouo5bkVAe%2BJSijQKIs5zALRa5C55YfZ%2Fbrz6PedFx4W40MZieGsxC0hpWd5tak5sGV4l%2F8CqoNhhBp5iJbdYKelKgzjd5TZX4Jd5Z%2F%2Ba8SbJUmXAeRtQorDuZGNvadHip1dLxKg%3D&AWSAccessKeyId=ASIAQ3PHCVTY5PNGUQSF&Expires=1558299152&Signature=T%2FF9LDbMObj452DgdIRBgc72B7M%3D&hash=c1e2c25ec823af6e36abbf6ee263e6872fdd54a9501dd2af608ba7a8cc2e26ab&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0169023X06000218&tid=spdf-62302666-9863-43ba-b4dd-8f46a74e3f14&sid=49cc69184040e2403819e8f2754829cf9b9cgxrqa&type=client)
</code>

This implementation is slightly different from others out there as focuses on the hourly patterns in a day - the temporal difference between any 2 objects is calcualted based on the absolute hour difference. 

Eg 1: 

object 1 occurred on May 20, 2019 8 am,   object 2 occurred on April 30, 2018 8am

the temporal difference between these 2 objects is 0

Eg 2: 

object 1 occurred on May 20, 2019 11 pm,   object 2 occurred on April 30, 2018 1am

the temporal difference between these 2 objects is 2
