//
//  stuff.swift
//  FormalDinnerSeating
//
//  Created by Charlie Heyman on 2/21/20.
//  Copyright © 2020 Cate. All rights reserved.
//

import Foundation

enum StudentError: Error{
    case noDataAvailable
    case canNotProcessData
}

struct Request {
    let reqURL:URL
    init() {
        let reqString = "http://localhost"
        guard let reqURL = URL(string: reqString) else {fatalError()}
        self.reqURL = reqURL
        
    }
    
    func getStudents(completion: @escaping(Result<list, StudentError>) -> Void) {
        let dataTask = URLSession.shared.dataTask(with: reqURL){ data, _, _ in
        guard let Data = data else {
            completion(.failure(.noDataAvailable))
            return
        }
        do {
            let decoder = JSONDecoder()
            // print(Data)
            let response = try decoder.decode(list.self, from: Data)
            //print("in function getStudents")
            //print(response)
            // return info to caller if success
            completion(.success(response))
        } catch {
            completion(.failure(.canNotProcessData))
        }
        }
    dataTask.resume()
   
    }
    
}


