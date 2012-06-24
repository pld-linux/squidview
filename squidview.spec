Summary:	A console program to nicely view squid's log
Summary(pl):	Konsolowy program pozwalaj�cy ogl�da� logi squida
Name:		squidview
Version:	0.63
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.rillion.net/squidview/%{name}-%{version}.tar.gz
# Source0-md5:	16ad2d5840b307a3c0701de310d8a57c
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

%description -l pl
Squidview jest interaktywnym konsolowym programem, kt�ry monitoruje
logi squida i wy�wietla je w przyjemny spos�b. Ma funkcje szukania i
raportowania, daj�c informacje takie jak przepustowo�� na u�ytkownika
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
