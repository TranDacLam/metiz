jQuery.extend(jQuery.jtsage.datebox.prototype.options.lang, {
  'vi': {
    setDateButtonLabel: "Chọn ngày",
    setTimeButtonLabel: "Set Time",
    setDurationButtonLabel: "Set Duration",
    todayButtonLabel: "Jump to Today",
    titleDateDialogLabel: "Chọn ngày",
    titleTimeDialogLabel: "Set Time",
    daysOfWeek: [
       'Chủ nhật', 'Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy'
    ],
    daysOfWeekShort: ["CN", "T2", "T3", "T4", "T5", "T6", "T7"],
    monthsOfYear: [
      "Tháng 1", "Tháng 2", "Tháng 3",
      "Tháng 4", "Tháng 5", "Tháng 6",
      "Tháng 7", "Tháng 8", "Tháng 9",
      "Tháng 10", "Tháng 11", "Tháng 12"
    ],
    monthsOfYearShort: [
      "TH1", "TH2", "TH3",
      "TH4", "TH5", "TH6",
      "TH7", "TH8", "TH9",
      "TH10", "TH11", "TH12"
    ],
    durationLabel: ["Days", "Hours", "Minutes", "Seconds"],
    durationDays: ["Day", "Days"],
    tooltip: "Open Date Picker",
    nextMonth: "Next Month",
    prevMonth: "Previous Month",
    timeFormat: 12,
    headerFormat: "%-d, %B, %Y",
    dateFieldOrder: ["d", "m", "y"],
    timeFieldOrder: ["h", "i", "a"],
    slideFieldOrder: ["y", "m", "d"],
    dateFormat: "%d-%m-%Y",
    useArabicIndic: false,
    isRTL: false,
    calStartDay: 0,
    clearButton: "clear",
    durationOrder: ["d", "h", "i", "s"],
    meridiem: ["AM", "PM"],
    timeOutput: "%k:%M", // 12hr: "%l:%M %p", 24hr: "%k:%M",
    durationFormat: "%Dd %DA, %Dl:%DM:%DS",
    calDateListLabel: "Other Dates",
    calHeaderFormat: "%B %Y",
    tomorrowButtonLabel: "Jump to Tomorrow"
  }
});
jQuery.extend(jQuery.jtsage.datebox.prototype.options, {
  useLang: 'vi'
});