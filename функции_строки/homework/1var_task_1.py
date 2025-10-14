ping = [input().strip() for _ in range(5)]
name = ping[0].split()[1]
times = [int(i.split("Time=")[1]) for i in ping[1:] if i.startswith("Reply from")]
sent = 4
received = len(times)
lost = sent - received
percent_loss = round(100 * lost / sent)
print(f"Ping statistics for {name}:\nPackets: Sent = {sent}, Received = {received}, Lost = {lost} ({percent_loss}% loss),\nApproximate round trip times in milli-seconds:\nMinimum = {min(times)}ms, Maximum = {max(times)}ms, Average = {round(sum(times)/received)}ms" if received else "")
