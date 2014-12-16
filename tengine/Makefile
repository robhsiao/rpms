spec = luv-tengine.spec
all: build dist

download:
	spectool -g -R $(spec)

rebuild:
	rpmbuild --short-circuit -bi $(spec)

build: download
	rpmbuild -bb $(spec)

dist:
	find ~/rpmbuild/RPMS -name "*.rpm" | xargs -I{} mv "{}" .

clean:
	rm ~/.rpmmacros
	rm -rf ~/rpmbuild
	rpmdev-setuptree
