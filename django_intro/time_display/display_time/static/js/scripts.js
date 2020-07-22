let currentDate = new Date()
let dateObj = {
    'year': currentDate.getFullYear(),
    'month': currentDate.getMonth() + 1,
    'day': currentDate.getDate(),
    'hour': currentDate.getHours(),
    'minute': currentDate.getMinutes(),
    'constructDateString': function() {
        let dateStr = this.month + '/' + this.day + '/' + this.year
        let timeStr = this.hour + ':' + this.minute
        return [dateStr, timeStr]
    }
}

$('#date').html(dateObj.constructDateString()[0])
$('#time').html(dateObj.constructDateString()[1])