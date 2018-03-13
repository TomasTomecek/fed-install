Name:           fed-install
Version:        0.1.0
Release:        1%{?dist}
Summary:        Install packages from specific Fedora releases or even from koji

License:        MIT
URL:            https://github.com/TomasTomecek/fed-install
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  /usr/bin/go-md2man

Requires:       createrepo_c
Requires:       dnf
Requires:       koji
Requires:       python3

%description
Install packages from specific Fedora releases or even from koji.


%prep
%autosetup -p1 -n %{name}-%{version}


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
* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Initial RPM release
