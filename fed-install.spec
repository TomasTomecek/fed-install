%global commit          b14bff2ccbf7da61dc06c0e90a111590dc18e8f5
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20171201

Name:           fed-install
Version:        0
Release:        0.1.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Install packages from specific Fedora releases or even from koji

License:        MIT
URL:            https://github.com/TomasTomecek/fed-install
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  /usr/bin/go-md2man

Requires:       createrepo_c
Requires:       dnf
Requires:       koji
Requires:       python3

%description
Install packages from specific Fedora releases or even from koji.


%prep
%autosetup -p1 -n %{name}-%{commit}


%build
go-md2man -in docs/%{name}.1.md -out docs/%{name}.1


%install
install -Dpm0644 docs/%{name}.1 \
    %{buildroot}%{_mandir}/man1/%{name}.1
install -Dpm0755 %{name} \
    %{buildroot}%{_bindir}/%{name}
  

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20171201gitb14bff2
- Initial RPM release
