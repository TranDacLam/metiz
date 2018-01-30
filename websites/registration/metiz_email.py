# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.core.mail import EmailMultiAlternatives, send_mail as send_mail_sy
from html2text import html2text
from django.conf import settings
from django.template import Context, Template
from django.template.loader import get_template
from django.contrib.sites.models import Site
import os


def send_mail_plantext(subject, message_plain, email_from, email_to, obj_model):
    """ Inherit send mail of django """
    if not message_plain:
        raise ValueError(
            _("Either message_plain or message_html should be not None"))

    if not email_from:
        email_from = settings.DEFAULT_FROM_EMAIL

    """ initial data using bind value to template """
    current_site = Site.objects.get_current()
    data = {'current_site': current_site, 'obj': obj_model}
    cxt = Context(data)

    """ bind data to template """
    text_content = get_template(message_plain).render(cxt)

    """ send email """
    send_mail_sy(subject, text_content, email_from,
                 email_to, fail_silently=False)


def send_mail(subject, message_plain, message_html, email_from, email_to,
              data_binding, custom_headers={}, attachments=(), att_files=None, email_cc=None):
    """
    Build the email as a multipart message containing
    a multipart alternative for text (plain, HTML) plus
    all the attached files.
    """
    try:
        if not message_html:
            raise ValueError(_("Either message_html should be not None"))

        if not message_plain:
            path_html = os.path.join(
                settings.BASE_DIR + '/templates/', message_html)
            message_plain = html2text(open(path_html).read())

        if not email_from:
            email_from = settings.DEFAULT_FROM_EMAIL

        """ initial data using bind value to html template """
        current_site = Site.objects.get_current()
        # data = { 'current_site':current_site, 'obj': obj_model }
        data = data_binding

        cxt = Context(data)
        """ bind data to html template """
        text_content = Template(message_plain).render(cxt)
        html_content = get_template(message_html).render(cxt)
        message = {}

        message['subject'] = subject
        message['body'] = text_content
        message['from_email'] = email_from
        message['to'] = email_to
        
        if email_cc:
            message['cc'] = email_cc

        if custom_headers:
            message['headers'] = custom_headers

        msg = EmailMultiAlternatives(**message)
        """ attach file in email """
        if attachments:
            try:
                for img in attachments:
                    msg.attach_file(settings.BASE_DIR + '/public' + img)
            except:
                pass

        if att_files:
            for f in att_files:
                msg.attach(att_files[f].name, att_files[
                           f].read(), att_files[f].content_type)

        if message_html:
            msg.attach_alternative(html_content, "text/html")
        return msg.send()
    except Exception, e:
        print "Send mail error ", e
        pass

# send_mail(subject, message_plain, message_html, email_from, [mailer.email_address], obj_model)
