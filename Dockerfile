FROM python:3.8
EXPOSE 8501
RUN pip3 install streamlit
COPY app.py /var/dashboard/app.py
CMD streamlit run /var/dashboard/app.py
