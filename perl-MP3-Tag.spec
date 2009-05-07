%define module	MP3-Tag
%define name	perl-%{module}
%define version 1.00
%define release %mkrel 2
%define _requires_exceptions perl(\\(Normalize::Text::Normalize_Fields\\|Music_Normalize_Fields\\))


Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Module for reading tags of MP3 audio files 
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/MP3/%{module}-%{version}.tar.bz2
Requires:	    perl(Compress::Zlib)
BuildRequires:	perl(Compress::Zlib)
BuildArch:	    noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Tag is a wrapper module to read different tags of mp3 files. It provides an
easy way to access the functions of separate modules which do the handling
of reading/writing the tags itself.

At the moment MP3::Tag::ID3v1 and MP3::Tag::ID3v2 are supported for read and
write; MP3::Tag::Inf, MP3::Tag::CDDB_File, MP3::Tag::File,
MP3::Tag::LastResort are supported for read access (the information obtained
by parsing CDDB files, .inf file and the filename).

%prep
%setup -q -n %{module}-%{version}
# requires CDDB connection
rm -f t/mp3tag.t
chmod -R u+w examples
chmod 755 examples/*.pl examples/mp3info2 examples/typeset_audio_dir

%build
# -n is here to avoid installation of scripts (they come in examples/ anyway)
%{__perl} Makefile.PL INSTALLDIRS=vendor -n
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README.txt TODO examples
%{perl_vendorlib}/MP3
%{perl_vendorlib}/Encode
%{perl_vendorlib}/Normalize
%{_mandir}/*/*

