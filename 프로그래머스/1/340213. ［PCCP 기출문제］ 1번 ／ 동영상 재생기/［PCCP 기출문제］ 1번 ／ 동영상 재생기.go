import (
	"fmt"
	"strconv"
	"strings"
)

func solution(video_len string, pos string, op_start string, op_end string, commands []string) string {
	videoSec := changeSec(video_len)
	posSec := changeSec(pos)
	startSec := changeSec(op_start)
	endSec := changeSec(op_end)

	if posSec >= startSec && posSec < endSec {
		posSec = endSec
	}

	for _, command := range commands {
		switch command {
		case "next":
			posSec += 10
		case "prev":
			posSec -= 10
		}

		if posSec < 0 {
			posSec = 0
		} else if posSec > videoSec {
			posSec = videoSec
		}
		if posSec >= startSec && posSec < endSec {
			posSec = endSec
		}
	}

	return fmt.Sprintf("%02d:%02d", posSec/60, posSec%60)
}

func changeSec(timeString string) int {
	time := strings.Split(timeString, ":")
	min, _ := strconv.Atoi(time[0])
	sec, _ := strconv.Atoi(time[1])

	sec += min * 60

	return sec
}
