# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from booking.models import MovieSync, BookingInfomation
from booking.forms import BookingForm
from booking import api
import json
import ast
from datetime import timedelta, datetime, time
from core.models import Movie

# Export to excel
import os
import xlsxwriter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
import os
from core.decorator import *

@check_user_booking_exist
def get_booking(request):
    try:
        """ Action render page booking for user selected chair,
            this action support for two action get and post
        """
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                full_name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                request.session['full_name'] = full_name
                request.session['phone'] = phone
                request.session['email'] = email if email else None

                id_showtime = form.cleaned_data['id_showtime']
                id_server = form.cleaned_data['id_server']
                movie_api_id = form.cleaned_data['movie_api_id']
                id_movie_name = form.cleaned_data['id_movie_name']
                id_movie_time = form.cleaned_data['id_movie_time']
                id_movie_date_active = form.cleaned_data[
                    'id_movie_date_active']
                print('*******booking******')
                return render(request, 'websites/booking.html', {"id_showtime": id_showtime, "id_server": id_server,
                                                                 "id_movie_name": id_movie_name, "id_movie_time": id_movie_time,
                                                                 "id_movie_date_active": id_movie_date_active,
                                                                 "movie_api_id": movie_api_id})
            else:
                return render(request, 'websites/booking.html')
        else:
            print('*******booking******')
            id_showtime = request.GET.get('id_showtime', "")
            id_server = request.GET.get('id_server', 1)
            movie_api_id = request.GET.get('movie_api_id', "")
            id_movie_name = request.GET.get('id_movie_name', "")
            id_movie_time = request.GET.get('id_movie_time', "")
            id_movie_date_active = request.GET.get('id_movie_date_active', "")
            return render(request, 'websites/booking.html', {"id_showtime": id_showtime, "id_server": id_server,
                                                             "id_movie_name": id_movie_name, "id_movie_time": id_movie_time,
                                                             "id_movie_date_active": id_movie_date_active,
                                                             "movie_api_id": movie_api_id})
    except Exception, e:
        print "Error get_booking : ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")


def time_out_booking(request):
    try:
        """ Action render page notification timeout for user """
        return render(request, 'websites/time_out_booking.html')
    except Exception, e:
        print "Error time out booking : ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")


def build_show_time_json(current_date, item, result, movies_info, obj_movie=None):
    """ Build Data Json For Movie ShowTime """

    # Check key not in result then create dictionary create new key
    # with data is list empty
    if item["MOVIE_ID"] not in result:
        # GET movie object by movie_api_id detail or get by MOVIE_ID
        if not obj_movie:
            obj_movie = movies_info.filter(
                movie_api_id=item["MOVIE_ID"])

        # obj_movie[0].name.split(':')[0] to get vietnames film names
        result[item["MOVIE_ID"]] = {"lst_times": [], "movie_id": item[
            "MOVIE_ID"], "movie_name": obj_movie[0].name.split(':')[0] if obj_movie else item["MOVIE_NAME_VN"],
            "rated": obj_movie[0].rated.name if obj_movie else None, "time_running": obj_movie[0].time_running if obj_movie else 0}

    # Check time showing greater than currnet hour
    if item["DATE"] == current_date.strftime("%d/%m/%Y"):
        current_time = (current_date.hour) * 60 + current_date.minute
        time_show = (int(item["TIME"].split(':')[0])) * \
            60 + int(int(item["TIME"].split(':')[1]))
        # compare hour and minute
        if time_show >= current_time:
            result[item["MOVIE_ID"]]["lst_times"].append(
                {"id_showtime": item["ID"], "time": item["TIME"], "room_name": item["ROOM_NAME"]})
    else:
        result[item["MOVIE_ID"]]["lst_times"].append(
            {"id_showtime": item["ID"], "time": item["TIME"], "room_name": item["ROOM_NAME"]})


def get_movie_show_time(request):
    try:
        """
            Get movie show times by date
        """
        current_date = timezone.localtime(timezone.now())

        date = request.GET.get('date', current_date.date())
        # cinema_id is equal id_server
        cinema_id = request.GET.get('cinema_id', 1)
        # movie_api_id = request.GET.get('movie_api_id', None)

        result = {}
        data_movie = MovieSync.objects.filter(
            name="showtime_current", date_show=date, cinema_id=cinema_id)

        """ Check query set and get first item """
        if data_movie:
            # Validate convert data to json
            try:
                show_string = json.loads(data_movie[0].data)
                show_times = ast.literal_eval(show_string)

                # get all movies
                movies_info = Movie.objects.filter(end_date__gte=date)
            except ValueError as e:
                print "Error get_movie_show_time convert json : %s" % e
                return JsonResponse({})

            # Generate dictionary result key is movie_id and values is time
            # showing
            # get movie object if movie_api_id not empty
            obj_movie = None
            # if movie_api_id:
            #     obj_movie = movies_info.filter(
            #         movie_api_id=movie_api_id.strip())

            for item in show_times["List"]:
                # Get Showtime movie by id
                # if movie_api_id:
                #     # Get Movie Name by movie api id
                #     if item["MOVIE_ID"].strip() == movie_api_id.strip():
                #         build_show_time_json(
                #             current_date, item, result, movies_info, obj_movie)
                # else:
                build_show_time_json(
                    current_date, item, result, movies_info)

        return JsonResponse(result)

    except Exception, e:
        print "Error get_movie_show_time : %s" % e
        return JsonResponse({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)


def get_seats(request):
    try:
        """
            Get seats by show times id
        """
        result = {"List": []}
        id_server = request.GET.get('id_server', 1)

        if 'id_showtime' in request.GET:
            result = api.call_api_seats(request.GET["id_showtime"], id_server)
            return JsonResponse(result)
        else:
            error = {"code": 500, "message": _("Fields id_showtime and id_server is required."),
                     "fields": "id_showtime, id_server"}
            return JsonResponse(error, status=500)

    except Exception, e:
        print "Error get_seats : %s" % e
        return JsonResponse({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)


def check_seats(request):
    try:
        """
            Action verify seats have been selected before
            - step 1 : verify if seat aready selected then response error
            - step 2 : Seats no have selected then post booking for user
        """
        if request.method == "POST":
            # Validate Request Parameter id_server and lst_seats
            id_server = request.POST.get('id_server', 1)
            if "lst_seats" not in request.POST or "id_showtime" not in request.POST or 'working_id' not in request.POST:
                return JsonResponse({"code": 400, "message": _("Fields lst_seats and id_showtime, working_id is required.")}, status=400)

            # Get new seats from api
            id_showtime = request.POST["id_showtime"]
            data_seats = api.call_api_seats(
                id_showtime, id_server)
            # get list chair of user selected
            seats_choice = ast.literal_eval(request.POST["lst_seats"])

            if data_seats and data_seats["List"] and seats_choice:
                seat_has_selected = []
                # check chairs of a user have been selected before
                for item in seats_choice:
                    chair = [str(s["NAME"]) for s in data_seats["List"] if s[
                        "ID"] == item["ID"] and s["STATUS"] == "True"]
                    if chair:
                        seat_has_selected.append(chair[0])

                if seat_has_selected:
                    return JsonResponse({"code": 400, "message": _("These chairs have been selected : %s" % seat_has_selected)}, status=400)
                else:
                    print "********** Post Booking Get Barcode **********"
                    # init url api without member card
                    url = "/postBooking"
                    # Call Booking Seats
                    full_name = request.session.get("full_name", "")
                    phone = request.session.get("phone", "")
                    email = request.session.get("email", "")
                    # Get Information of user and building data for api update
                    # status of seats
                    member_card = request.POST.get('member_card')
                    # Change api url when card member is not null
                    if member_card:
                        url = "/postBookingMember"

                    result = api.call_api_post_booking(
                        full_name, phone, email, seats_choice, id_server, member_card, url)

                    if not result["BARCODE"]:
                        print "***** Get Barcode Fail : ", result
                        return JsonResponse({"code": 400, "message": _("Cannot Booking Seats. Please Contact Administrator.")}, status=400)

                    print "***** Information User Booking , Full Name: %s, Member Card: %s, Phone: %s, Email: %s, Barcode: %s"%(full_name, member_card, phone, email, result["BARCODE"])
                    # Add Seats into session and set seats expire in five
                    # minute
                    current_store = request.session.get("movies", {})
                    working_id = request.POST["working_id"]
                    if working_id in current_store:
                        """
                            If session exist working_id then append new seat item into session:
                            Algorithm :
                             - Cancel seats old in workingid and add new seats choice
                        """
                        print "***** Working_id existing into sessions ", working_id
                        if current_store[working_id]["seats_choice"]:
                            for seat_id in current_store[working_id]["seats_choice"]:
                                print "***** Clear Old Seats of Working_id existing into sessions ", seat_id
                                api.call_api_cancel_seat(
                                    seat_id=seat_id, id_server=id_server)

                        print "***** Append New Seats for Working_id : ", seats_choice
                        current_store[working_id][
                            "seats_choice"] = seats_choice
                        current_store[working_id]["time_choice"] = timezone.localtime(timezone.now(
                        ) + timedelta(minutes=settings.TIME_SEAT_DELAY)).strftime("%Y-%m-%d %H:%M:%S.%f"),

                    else:
                        # Add new key as working_id in store movie session
                        print "***** Add Working_id in Sessions : %s and list seats : %s  "%(working_id, seats_choice)
                        current_store[working_id] = {
                            "time_choice": timezone.localtime(timezone.now() + timedelta(minutes=settings.TIME_SEAT_DELAY)).strftime("%Y-%m-%d %H:%M:%S.%f"),
                            "seats_choice": seats_choice,
                            "barcode": result["BARCODE"]
                        }
                    print "***** Store Booking in Session, Phone: %s, Email: %s, Barcode: %s, Data Store: %s "%(phone, email, result["BARCODE"], current_store)
                    request.session['movies'] = current_store

                    return JsonResponse(result)
    except Exception, e:
        print "Error booking_seats : %s" % e
        return JsonResponse({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)


def booking_payment(request):
    try:
        if request.method == "POST":
            # Validate Request Parameter id_server and lst_seats
            if "barcode" not in request.POST:
                return JsonResponse({"code": 400, "message": _("Fields barcode is required.")}, status=400)

            id_server = request.POST.get('id_server', 1)

            result_confirm = api.call_api_booking_confirm(
                request.POST["BARCODE"], id_server)

            return JsonResponse(result_confirm)

    except Exception, e:
        print "Error booking_payment : %s" % e
        return JsonResponse({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)


def clear_seats(request):
    try:
        if request.method == "POST":
            if "working_id" not in request.POST:
                return JsonResponse({"code": 400, "message": _("Fields working_id is required.")}, status=400)

            id_server = request.POST.get("id_server", 1)
            working_id = request.POST["working_id"]
            movie_store = request.session.get("movies", {})
            # Check Working id exist in session and remove it
            if movie_store and working_id in movie_store:
                for seat_id in movie_store[working_id]["seats_choice"]:
                    print "##### Clear Seat ", seat_id
                    api.call_api_cancel_seat(
                        seat_id=seat_id["ID"], id_server=id_server)
                del movie_store[working_id]

                if movie_store:
                    request.session["movies"] = movie_store
                else:
                    del request.session["movies"]
            return JsonResponse({"result": True})
    except Exception, e:
        print "Error clear_seats : %s ", e
        pass


""" START BOOKING INFORMATION REPORT """


def booking_info_data(request):
    try:
        booking_info_list = BookingInfomation.objects.all().order_by('-created')
        
        # Get Parameter From POST request
        order_id = request.POST.get("order_id", "1")
        order_status = request.POST.getlist("order_status[]", [])
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        barcode = request.POST.get("barcode", "")
        date_from = request.POST.get("date_from", "")
        date_to = request.POST.get("date_to", "")

        print "order_status", order_status

        kwargs = {}

        # If paramter is not null then append condition to query
        if order_id:
            kwargs['order_id'] = order_id
        if order_status:
            kwargs['order_status__in'] = order_status
        if email:
            kwargs['email'] = email
        if phone:
            kwargs['phone'] = phone
        if barcode:
            kwargs['barcode'] = barcode
        if date_from:
            kwargs['created__gte'] = datetime.combine(datetime.strptime(date_from, "%d/%m/%Y").date(), time.min)
        if date_to:
            kwargs['created__lte'] = datetime.combine(datetime.strptime(date_to, "%d/%m/%Y").date(), time.max)
        if kwargs:
            booking_info_list = booking_info_list.filter(**kwargs)

        return booking_info_list

    except DatabaseError, e:
        print "ERROR Connect DB: ", e
        raise Exception(
            "Connect DB Error .Please contact administrator.")


def booking_info_data_mapping(booking_info_list):
    booking_info_results = []
    if booking_info_list:
        for booking_info in booking_info_list:
            info = {}
            info['order_id'] = booking_info.order_id
            info['order_desc'] = booking_info.order_desc
            info['order_status'] = booking_info.order_status
            info['desc_transaction'] = booking_info.desc_transaction
            info['barcode'] = booking_info.barcode
            info['amount'] = int(booking_info.amount)
            info['email'] = booking_info.email
            info['phone'] = booking_info.phone
            info['created_format'] = timezone.localtime(booking_info.created).strftime('%d/%m/%Y %H:%M')
            info['full_name'] = '' if booking_info.user is None else booking_info.user.full_name
            booking_info_results.append(info)
    return booking_info_results

@login_required(login_url='/admin/login/')
@permission_required('is_superuser', login_url='/admin/login/')
def booking_info_report(request):
    try:
        if request.method == "POST":
            result = {}
            # Get start index
            start = int(request.POST.get("start"))
            # End index = start index + length
            end = start + int(request.POST.get("length"))

            # Get data booking information
            booking_info_list = booking_info_data(request)

            # Get total items result
            total_items = len(booking_info_list)

            # Get Booking information from start to end
            booking_info_list = booking_info_list[start:end]

            result["data"] = booking_info_data_mapping(booking_info_list)
            result["recordsTotal"] = total_items
            result["recordsFiltered"] = total_items

            return HttpResponse(
                json.dumps(result),
                content_type="application/json"
            )
    except Exception, e:
        print "Error booking_info_report : %s ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")

    return render(request, "websites/booking/booking_info_report.html")


@login_required(login_url='/admin/login/')
@permission_required('is_superuser', login_url='/admin/login/')
def booking_info_export_to_excel(request):

    try:
        if request.method == 'POST':
            # Get total items result
            booking_info_list = booking_info_data(request)

            if booking_info_list:
                excel_file_name = "BookingInformationReport.xlsx"
                booking_info_result = booking_info_data_mapping(booking_info_list)
                # Export to excel
                write_to_excel(excel_file_name, booking_info_result)
                return HttpResponse(
                    json.dumps(
                        {"uri": '/media/excel/' + excel_file_name}),
                    content_type="application/json"
                )
        return HttpResponse(
            json.dumps({"uri": '#'}),
            content_type="application/json"
        )
    except Exception, e:
        print "Error booking_info_report : %s ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")


"""
    Get root folder path.
"""


def get_root_folder():
    BASE_DIR = os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    ROOT_FOLDER = os.path.join(BASE_DIR, "public/media", "excel")
    if not os.path.isdir(ROOT_FOLDER):
        os.makedirs(ROOT_FOLDER)
    return ROOT_FOLDER


"""
    Write Data to excel file
"""


def write_to_excel(file_name, booking_list):

    try:

        # Get folder contain excel file
        ROOT_FOLDER = get_root_folder()

        # create workbook
        workbook = xlsxwriter.Workbook(
            os.path.join(ROOT_FOLDER, file_name))

        worksheet = workbook.add_worksheet()

        title = "Booking Information"
        # header format
        header_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#739abb',
            'font_color': '#ffffff'})
        # merge format
        merge_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#ffffff',
            'font_size': 24})
        # ceate money format in worksheet
        money_format = workbook.add_format({'num_format': '#,##0'})
        cell_format = workbook.add_format({'text_wrap': True, 'valign': 'top'})

        worksheet.merge_range('A1:J1', title, merge_format)

        # set header of excel
        worksheet.write('A2', 'Order ID', header_format)
        worksheet.write('B2', 'Order Description', header_format)
        worksheet.write('C2', 'Order Status', header_format)
        worksheet.write('D2', 'Order Transaction', header_format)
        worksheet.write('E2', 'Barcode', header_format)
        worksheet.write('F2', 'Amount', header_format)
        worksheet.write('G2', 'Full Name', header_format)
        worksheet.write('H2', 'Email', header_format)
        worksheet.write('I2', 'Phone', header_format)
        worksheet.write('J2', 'Created Date', header_format)

        # set width of cell
        worksheet.set_column(0, 0, 17)
        worksheet.set_column(1, 1, 35)
        worksheet.set_column(2, 2, 13)
        worksheet.set_column(3, 3, 20)
        worksheet.set_column(4, 4, 10)
        worksheet.set_column(5, 5, 15)
        worksheet.set_column(6, 6, 20)
        worksheet.set_column(7, 7, 25)
        worksheet.set_column(8, 8, 15)
        worksheet.set_column(9, 9, 20)
        worksheet.set_row(0, 40)
        worksheet.set_row(1, 30)

        # fill Data to excel
        if booking_list:
            row = 2
            for booking in booking_list:
                worksheet.write(row, 0, booking["order_id"])
                worksheet.write(row, 1, booking["order_desc"], cell_format)
                worksheet.write(row, 2, booking["order_status"])
                worksheet.write(row, 3, booking["desc_transaction"])
                worksheet.write(row, 4, booking["barcode"])
                worksheet.write(row, 5, booking["amount"], money_format)
                worksheet.write(row, 6, booking["full_name"])
                worksheet.write(row, 7, booking["email"])
                worksheet.write(row, 8, booking["phone"])
                worksheet.write(row, 9, booking["created_format"])
                row += 1

        workbook.close()

    except Exception, e:
        print "Error write_to_excel : %s ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")
""" END BOOKING INFORMATION REPORT """

@login_required(login_url='/admin/login/')
@permission_required('is_superuser', login_url='/admin/login/')
def movies_synchronize(request):
    try:
        if request.method == "POST":
            os.system("fab synchronize")
            return JsonResponse({"message": "Success Synchronize movies."}, status=200)
        else:
            return render(request, 'websites/booking/movies_synchronize.html')
    except Exception, e:
        print "Error Action movies_synchronize : ",e
        return JsonResponse({"message": "Cannot synchronize movies. Please contact administrator "}, status=500)
