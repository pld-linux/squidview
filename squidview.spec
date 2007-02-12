Summary:	A console program to nicely view squid's log
Summary(pl.UTF-8):   Konsolowy program pozwalający oglądać logi squida
Name:		squidview
Version:	0.69
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.rillion.net/squidview/%{name}-%{version}.tar.gz
# Source0-md5:	b9691075e44f7ae5f6ca7ebcc36e8327
Patch0:		%{name}-pld.patch
Patch1:		%{name}-curses,howto-dest.patch
URL:		http://www.rillion.net/squidview/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Squidview is an interactive console program which monitors squid logs
and displays them in a nice fashion. It has searching and reporting
functions, giving information like per user bandwidth and cache hits.

%description -l pl.UTF-8
Squidview jest interaktywnym konsolowym programem, który monitoruje
logi squida i wyświetla je w przyjemny sposób. Ma funkcje szukania i
raportowania, dając informacje takie jak przepustowość na użytkownika
i trafienia cache-a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	CXXFLAGS="-I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog HOWTO README users words aliases
%attr(754,root,root) %{_bindir}/*
