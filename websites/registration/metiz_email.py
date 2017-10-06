# -*- coding: utf-8 -*-
import re
from StringIO import StringIO
from django.utils.translation import ugettext as _
from django.core.mail import EmailMultiAlternatives, send_mail as send_mail_sy
from html2text import html2text as html2text_orig
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.contrib.sites.models import Site


LINK_RE = re.compile(r"https?://([^ \n]+\n)+[^ \n]+", re.MULTILINE)
def html2text(html):
    """Use html2text but repair newlines cutting urls.
    Need to use this hack until
    https://github.com/aaronsw/html2text/issues/#issue/7 is not fixed"""
    txt = html2text_orig(html)
    links = list(LINK_RE.finditer(txt))
    out = StringIO()
    pos = 0
    for l in links:
        out.write(txt[pos:l.start()])
        out.write(l.group().replace('\n', ''))
        pos = l.end()
    out.write(txt[pos:])
    return out.getvalue()

def send_mail_plantext(subject, message_plain, email_from, email_to, obj_model):
    """ Inherit send mail of django """
    if not message_plain:
        raise ValueError(_("Either message_plain or message_html should be not None"))

    if not email_from:
        email_from = settings.DEFAULT_FROM_EMAIL

    """ initial data using bind value to template """
    current_site = Site.objects.get_current()
    data = { 'current_site':current_site, 'obj': obj_model }
    cxt = Context(data)

    """ bind data to template """
    text_content = get_template(message_plain).render(cxt)

    """ send email """
    send_mail_sy(subject, text_content, email_from,
    email_to, fail_silently=False)


def send_mail(subject, message_plain, message_html, email_from, email_to,
              data_binding, custom_headers={}, attachments=(), att_files=None):
    """
    Build the email as a multipart message containing
    a multipart alternative for text (plain, HTML) plus
    all the attached files.
    """

    if not message_plain and not message_html:
        raise ValueError(_("Either message_plain or message_html should be not None"))

    if not message_plain:
        message_plain = html2text(message_html)

    if not email_from:
        email_from = settings.DEFAULT_FROM_EMAIL

    """ initial data using bind value to html template """
    current_site = Site.objects.get_current()
    # data = { 'current_site':current_site, 'obj': obj_model }
    data = data_binding

    cxt = Context(data)
    """ bind data to html template """
    text_content = get_template(message_plain).render(cxt)
    html_content = get_template(message_html).render(cxt)
    message = {}

    message['subject'] = subject
    message['body'] = text_content
    message['from_email'] = email_from
    message['to'] = email_to
    # if attachments:
    #     message['attachments'] = attachments
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
            msg.attach(att_files[f].name, att_files[f].read(), att_files[f].content_type)

    if message_html:
        msg.attach_alternative(html_content, "text/html")
    return msg.send()

# send_mail(subject, message_plain, message_html, email_from, [mailer.email_address], obj_model)
