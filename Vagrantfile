# -*- mode: ruby -*-
# vi: set ft=ruby :

boxes = {
  'debian8' => 'debian/jessie64',
  'debian9' => 'debian/stretch64',
  'centos6' => 'centos/6',
  'centos7' => 'centos/7'
}

Vagrant.configure('2') do |config|
  # Start multiple virtual machines with each supported operating system
  # to test the functionality. All hosts will managed via anisble.

  boxes.each do |name, boxtype|
    config.vm.define name.to_s do |node|
      # boxtype is operating system see boxes hash.
      node.vm.box = boxtype.to_s
      # provisioning over ansible playbook
      node.vm.provision 'ansible_local' do |ansible|
        ansible.sudo = true
        ansible.verbose = true
        ansible.playbook = "build/ansible/playbook-#{name}.yml"
      end
    end
  end

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
end
