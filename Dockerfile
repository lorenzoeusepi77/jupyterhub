FROM jupyterhub/jupyterhub


#POSTGRES DB PACKAGE
RUN apt-get update && \
    apt-get install -y \
        libpq-dev \
        npm \ 
 && apt-get autoremove -y \
 && apt-get clean -y \
 && pip install psycopg2 

#    pip install jupyterhub-ldapauthenticator
 

# ADD LDAP AUTH PACKAGE
RUN pip install jupyterhub-ldapauthenticator
RUN pip install jupyterhub-ldapcreateusers

# ADD LOCAL USER
RUN useradd -m -G shadow -p $(openssl passwd -1 rhea) rhea
RUN chown rhea .
RUN useradd -m -G shadow -p $(openssl passwd -1 lorenzo) lorenzo
RUN chown lorenzo .


RUN for name in io ganymede ; do useradd -m -p $(openssl passwd -1 $name) $name; done

# ADD Configurable-http-proxy
#RUN npm install -g configurable-http-proxy
RUN pip install notebook

#EXPOSE 8000
ENTRYPOINT ["jupyterhub"]

USER root
